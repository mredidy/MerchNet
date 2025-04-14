# MerchNet – Real-Time Ethereum PYUSD Transactions 💰📊

## Overview 🚀
MerchNet is a real-time analytics tool that fetches Ethereum blockchain transaction data for PayPal's PYUSD token. This script extracts the latest PYUSD transaction data from BigQuery, formats it into a pandas dataframe, and updates a Google Sheet with the transaction details. The sheet includes information such as transaction hashes, sender and receiver addresses, transaction value in PYUSD, and links to Etherscan for each transaction.

The script automates the process of fetching, formatting, and presenting real-time Ethereum transactions in an easy-to-read Google Sheet for monitoring purposes.

[Test the script here](https://colab.research.google.com/github/mredidy/MerchNet/blob/main/MerchNet_Analytics.ipynb)
## Features ⭐
- **Real-time Data Fetching**: Fetches the latest PYUSD transaction data from BigQuery. ⏱️
- **Google Sheets Integration**: Updates a designated Google Sheet with the latest data, including links to transaction details on Etherscan. 📑🔗
- **Data Formatting**: Converts transaction values to a human-readable format (e.g., formatted to two decimal places) and adds transaction hash links to Etherscan. 🔢✨
- **Sheet Customization**:
  - Adds alternating row colors for better readability. 🌈
  - Adjusts column widths based on content. 📏
  - Formats headers to be bold and center-aligned. 🔠
- **Error Handling**: Includes basic error handling to catch and log issues encountered during execution. ⚠️


## Video 🎥
Watch the demo video to see **MerchNet** in action! This video demonstrates how to fetch real-time Ethereum PYUSD transactions and automatically update the Google Sheet.

[![Watch the demo video](https://img.youtube.com/vi/YOUR_VIDEO_ID/0.jpg)](https://www.youtube.com/watch?v=YOUR_VIDEO_ID)

## Requirements 📦
Before running this script, ensure you have the following Python libraries installed:

- `google-cloud-bigquery` — For querying data from Google BigQuery. ☁️
- `google-auth` — For authentication with Google Cloud services. 🔐
- `gspread` — For interacting with Google Sheets. 🗂️
- `gspread-dataframe` — For updating Google Sheets with pandas dataframes. 📈
- `gspread-formatting` — For formatting cells in Google Sheets. ✏️
- `pandas` — For data manipulation and formatting. 🧑‍💻

You can install these dependencies using the following command:

`bash
pip install google-cloud-bigquery google-auth gspread gspread-dataframe gspread-formatting pandas

## Setup 🛠️

### Google Cloud Setup 🌐:
1. Create a service account in your Google Cloud project with permissions to access BigQuery, Google Sheets, and Google Drive.
2. Download the service account key (JSON file) and save it in your local environment.
3. Replace the path in the script `SERVICE_ACCOUNT_FILE` with the path to your service account key.

### BigQuery Setup 📊:
1. Make sure the `bigquery-public-data.crypto_ethereum.token_transfers` dataset is accessible and that you have permissions to query it.
2. The script queries the PYUSD token contract address on Ethereum: `0x6c3ea9036406852006290770bedfcaba0e23a0e8`.

### Google Sheets Setup 📑:
1. Create a Google Sheet named `MerchNet`.
2. Ensure the service account has write access to the sheet.
3. The script will create a new worksheet named `Ethereum` if it doesn’t exist, or it will update the existing one.

### Authentication 🔑:
1. Use Google service account credentials to authenticate the script.
2. The credentials must include permissions for BigQuery, Google Sheets, and Google Drive.

---

## How to Run 🏃‍♂️

### Set Up the Script 📝:
1. Download the Python script (e.g., `merchnet_update.py`) and modify the paths for `SERVICE_ACCOUNT_FILE` and `SPREADSHEET_NAME`.
2. Ensure your Google Cloud project ID is correctly set in `PROJECT_ID`.

### Execute the Script ▶️:
Run the script in your Python environment. The script will:
1. Query BigQuery for the latest 100 PYUSD Ethereum transactions. 🧐
2. Format the transaction data into a dataframe. 📊
3. Update the `Ethereum` worksheet in your Google Sheet. 📋

`bash
python merchnet_update.py

## Automate the Updates (Optional) ⏰:
You can schedule this script to run periodically using Google Cloud Scheduler or a cron job to keep the data updated in real-time. 🔄

---

## Code Explanation 🧑‍💻

### Main Components:

#### BigQuery Client 🏷️:
The script uses the BigQuery client to query the public Ethereum transaction data for the PYUSD token. The query fetches the latest 100 transactions, including the block timestamp, sender's and receiver's addresses, transaction hash, and block number.

#### Google Sheets Integration 🗂️:
The script uses `gspread` to interact with Google Sheets, updating or creating a worksheet to store the transaction data. The sheet is formatted with bold headers, alternating row colors, and dynamically adjusting column widths.

#### Data Formatting 💵:
The transaction values are converted to USD format (with two decimal places), and Etherscan links are generated for each transaction. 🔗

#### Error Handling ⚠️:
The script includes basic error handling to log any issues that occur during the execution of the data retrieval or sheet update process.

---

## Example Output in Google Sheets 💼

| Block Timestamp     | Sender's Address                         | Receiver's Address                       | Amount in $PYUSD | Contract Address                            | Transaction Hash       | Block  | Etherscan Link                   |
|---------------------|------------------------------------------|------------------------------------------|------------------|---------------------------------------------|------------------------|--------|----------------------------------|
| 2025-04-14 10:10:00 | 0x1234abcd...                            | 0x5678efgh...                            | 500.00           | 0x6c3ea9036406852006290770bedfcaba0e23a0e8 | 0xabcdef1234567890...  | 123456 | [View Transaction](https://etherscan.io/tx/0xabcdef1234567890...) |

---

## Troubleshooting 🛠️

- **Missing Google Sheets**: Ensure that the service account has write access to the Google Sheet. 📝
- **Query Failures**: If the BigQuery query fails, check the permissions of the service account and the availability of the public dataset. ⚠️
- **Authentication Errors**: Ensure the correct service account credentials are being used. 🔐

---

## License 📄
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 📝

---

## Notes 📝:
- Make sure you update the paths for your `SERVICE_ACCOUNT_FILE` and `SPREADSHEET_NAME` before running the script.
- You can also automate running the script by using services like Google Cloud Scheduler or cron jobs if you wish to keep the data up-to-date regularly. 🔄

## Author ✍️
This project is developed by **[Mister Edidy](https://twitter.com/mister_edidy)**. Feel free to reach out for any questions or suggestions!

Twitter: [@mister_edidy](https://twitter.com/mister_edidy)  
GitHub: [mredidy](https://github.com/mredidy)



