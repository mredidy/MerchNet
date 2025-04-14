from google.cloud import bigquery, secretmanager
from google.oauth2 import service_account
import gspread
from gspread_dataframe import set_with_dataframe
from gspread_formatting import set_column_width
import pandas as pd
import tempfile

PROJECT_ID = 'red-parity-456515-t4'
SPREADSHEET_NAME = 'MerchNet Insights'
SECRET_ID = 'merchnet-service-account'

SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/bigquery'
]

def get_service_account_credentials(secret_id=SECRET_ID):
    client = secretmanager.SecretManagerServiceClient()
    name = f"projects/{PROJECT_ID}/secrets/{secret_id}/versions/latest"
    response = client.access_secret_version(name=name)
    secret_data = response.payload.data.decode("UTF-8")

    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".json")
    temp_file.write(secret_data.encode())
    temp_file.close()
    return temp_file.name

def update_sheet():
    try:
        SERVICE_ACCOUNT_FILE = get_service_account_credentials()

        credentials = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES
        )
        bq_client = bigquery.Client(credentials=credentials, project=PROJECT_ID)
        gs_client = gspread.authorize(credentials)
        spreadsheet = gs_client.open(SPREADSHEET_NAME)
        worksheet = spreadsheet.sheet1
        worksheet_id = worksheet._properties['sheetId']

        query = """
        SELECT
          block_timestamp AS `Block Timestamp`,
          LOWER(from_address) AS `Sender's Address`,
          LOWER(to_address) AS `Receiver's Address`,
          CAST(value AS FLOAT64) / 1e6 AS Value,
          token_address AS `Contract Address`,
          transaction_hash AS `Transaction Hash`,
          block_number AS `Block`
        FROM `bigquery-public-data.crypto_ethereum.token_transfers`
        WHERE token_address = '0x6c3ea9036406852006290770bedfcaba0e23a0e8'
        ORDER BY block_timestamp DESC
        LIMIT 100
        """

        df = bq_client.query(query).to_dataframe()
        df["Etherscan Link"] = df["Transaction Hash"].map(
            lambda tx: f'=HYPERLINK("https://etherscan.io/tx/{tx}", "View Transaction")'
        )
        df["Amount in $PYUSD"] = df["Value"].map(lambda x: "{:,.2f}".format(x))
        df.drop(columns=["Value"], inplace=True)

        columns = [
            "Block Timestamp", "Sender's Address", "Receiver's Address",
            "Amount in $PYUSD", "Contract Address", "Transaction Hash", "Block", "Etherscan Link"
        ]
        df = df[columns]

        df_padded = df.copy()
        for col in df.columns:
            if col != "Etherscan Link":
                df_padded[col] = df[col].map(lambda x: f"          {x}" if pd.notnull(x) else "")

        def add_header_title():
            worksheet.update(values=[['📊 MerchNet – Live $PYUSD Transaction Monitor']], range_name='A1')
            spreadsheet.batch_update({
                "requests": [
                    {
                        "mergeCells": {
                            "range": {
                                "sheetId": worksheet_id,
                                "startRowIndex": 0,
                                "endRowIndex": 1,
                                "startColumnIndex": 0,
                                "endColumnIndex": len(df.columns)
                            },
                            "mergeType": "MERGE_ALL"
                        }
                    },
                    {
                        "repeatCell": {
                            "range": {
                                "sheetId": worksheet_id,
                                "startRowIndex": 0,
                                "endRowIndex": 1,
                                "startColumnIndex": 0,
                                "endColumnIndex": len(df.columns)
                            },
                            "cell": {
                                "userEnteredFormat": {
                                    "horizontalAlignment": "CENTER",
                                    "textFormat": {

    # === Write data ===
    set_with_dataframe(worksheet, df_padded, row=2)

    worksheet.format("A2:H2", {
        'textFormat': {'bold': True},
        'horizontalAlignment': 'CENTER'
    })

    # === Auto column width ===
    def get_column_letter(col_idx):
        letters = ''
        while col_idx >= 0:
            letters = chr(col_idx % 26 + 65) + letters
            col_idx = col_idx // 26 - 1
        return letters

    for i, col in enumerate(df_padded.columns):
        max_len = max(len(str(col)), df_padded[col].astype(str).apply(len).max()) + 2
        col_letter = get_column_letter(i)
        set_column_width(worksheet, f'{col_letter}:{col_letter}', max(100, min(max_len * 7, 400)))

    return "✅ MerchNet sheet updated!"

