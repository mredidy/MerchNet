import time
import pandas as pd
from google.cloud import bigquery
from google.oauth2 import service_account
import gspread
from gspread_dataframe import set_with_dataframe
from gspread_formatting import set_column_width

# ========== CONFIG ==========
SERVICE_ACCOUNT_FILE = 'MerchNet-Google-Sheets-API.json'
PROJECT_ID = 'your-gcp-project-id'
SPREADSHEET_NAME = 'MerchNet Insights'
# ============================

SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/bigquery'
]

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE,
    scopes=SCOPES
)
bq_client = bigquery.Client(credentials=credentials, project=PROJECT_ID)
gs_client = gspread.authorize(credentials)
spreadsheet = gs_client.open(SPREADSHEET_NAME)
worksheet = spreadsheet.sheet1
sheet_id = spreadsheet.id
worksheet_id = worksheet._properties['sheetId']

# ========== BigQuery Query ==========
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
# ====================================

def update_sheet():
    df = bq_client.query(query).to_dataframe()

    df["Etherscan Link"] = df["Transaction Hash"].apply(
        lambda tx: f'=HYPERLINK("https://etherscan.io/tx/{tx}", "View Transaction")'
    )
    df["Amount in $PYUSD"] = df["Value"].apply(lambda x: "{:,.2f}".format(x))
    df.drop(columns=["Value"], inplace=True)

    columns = [
        "Block Timestamp", "Sender's Address", "Receiver's Address",
        "Amount in $PYUSD", "Contract Address", "Transaction Hash", "Block", "Etherscan Link"
    ]
    df = df[columns]

    def pad_cell(x): return f"               {x}" if pd.notnull(x) else ""
    df_padded = df.map(pad_cell)

    worksheet.clear()
    worksheet.update(values=[['📊 MerchNet – Live $PYUSD Transaction Monitor']], range_name='A1')
    set_with_dataframe(worksheet, df_padded, row=2)
    worksheet.format("A2:H2", {'textFormat': {'bold': True}, 'horizontalAlignment': 'CENTER'})

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

    print(" MerchNet updated — Google Sheet is live and fresh!")

if __name__ == "__main__":
    update_sheet()
