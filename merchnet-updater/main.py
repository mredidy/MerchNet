from flask import Flask
from google.cloud import bigquery
from google.oauth2 import service_account
import gspread
from gspread_dataframe import set_with_dataframe
from gspread_formatting import set_column_width
import pandas as pd

# ====================== CONFIG ======================
SERVICE_ACCOUNT_FILE = 'MerchNet-Google-Sheets-API.json'
PROJECT_ID = 'red-parity-456515-t4'
SPREADSHEET_NAME = 'MerchNet Insights'
# ====================================================

SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/bigquery'
]

app = Flask(__name__)

def update_sheet():
    try:
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
                                        "bold": True,
                                        "fontSize": 20
                                    }
                                }
                            },
                            "fields": "userEnteredFormat(horizontalAlignment,textFormat)"
                        }
                    }
                ]
            })

        worksheet.clear()
        add_header_title()
        set_with_dataframe(worksheet, df_padded, row=2)

        worksheet.format("A2:H2", {
            'textFormat': {'bold': True},
            'horizontalAlignment': 'CENTER'
        })

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
    except Exception as e:
        return f"❌ Error: {str(e)}", 500

@app.route("/cron", strict_slashes=False)
def run_cron_job():
    try:
        result = update_sheet()
        return result
    except Exception as e:
        return f"❌ Cron error: {str(e)}", 500
        
@app.route("/health")
def health_check():
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
