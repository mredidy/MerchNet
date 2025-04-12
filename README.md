# MerchNet

MerchNet is a real-time crypto payment insights tool designed for local businesses to easily track and understand on-chain PayPal USD (PYUSD) transactions. Built with simplicity and practicality in mind, MerchNet enables merchants to monitor live transactions, analyze customer and merchant behavior, and get real-time visibility into blockchain flows without needing technical expertise.

## 🚀 Problem Statement

As crypto adoption grows, local merchants face challenges in tracking and interpreting blockchain transactions. MerchNet addresses this gap by offering a no-code solution that provides:

- Real-time monitoring of PYUSD payments
- Transaction metadata in a clean, human-readable format
- Insights into regional transaction flows (opt-in)
- Automatic logging and analysis in Google Sheets

## 🧩 Project Overview

MerchNet uses Etherscan and Google Cloud's Blockchain Node Engine APIs to deliver valuable insights, including:

- **Real-time PYUSD transaction tracking**
- **Known wallet labeling** (e.g., PayPal, exchanges, smart contracts)
- **Etherscan links** for direct access to transaction details
- **Google Sheets Sync** for easy tracking and analysis of transactions
- **Geographic insight** into regional transaction flows (optional)

## ✨ Features

- 🧾 **Live Etherscan API Integration:** Monitor real-time PYUSD transactions on the blockchain
- 🔗 **Etherscan Links:** Direct access to transaction details on-chain
- 🧠 **Known Wallet Labeling:** Contextual labels for known addresses (e.g., PayPal, exchanges)
- 📊 **Google Sheets Sync:** Automatically log transaction data for easy analysis
- 🌍 **Geographic Insight (Opt-in):** Gain insights into transaction flows by region (optional, privacy-respecting)
- 🧪 **Open Source:** 100% open-source and reproducible

## 🛠 Tech Stack

- **Python (Google Colab for development & runtime)**
- **Etherscan API** (to fetch blockchain data)
- **Google Sheets API** (for auto-logging and reporting)
- **Google Cloud Blockchain RPC** (planned for future integration)

## 🔄 How It Works

1. **Fetch Transactions:** The app uses the Etherscan API to fetch recent PYUSD transactions.
2. **Process Data:** Each transaction is processed to extract the sender, receiver, value, timestamp, and labels for known wallets.
3. **Update Google Sheets:** The transaction data, along with metadata and an Etherscan link, is logged in Google Sheets for further analysis.

## 🌍 Geographic Insight (Optional)

Merchants can opt into viewing regional transaction flows, helping them gain a better understanding of where transactions are originating. This feature is privacy-respecting and does not track individual user identities.

## 📝 Requirements

Before running this project, make sure you have the following:

- Python 3.x
- Google Cloud Project and enabled APIs (Google Sheets API and Google Cloud Blockchain RPC)
- Etherscan API Key
- A Google Sheets file with the appropriate credentials

Markdown

# 🏁 Getting Started with MerchNet

MerchNet is a tool designed to streamline the process of tracking and logging PYUSD transactions for local businesses, making cryptocurrency payments more accessible and understandable.

## 1. Clone the Repository

To get started, clone the MerchNet repository to your local machine:

```bash
git clone [https://github.com/mredidy/MerchNet.git](https://github.com/mredidy/MerchNet.git)
cd MerchNet
2. Install Dependencies
Ensure you have Python 3.x installed. Then, install the required dependencies using pip:

Bash

pip install -r requirements.txt
3. Set Up Google Sheets API
MerchNet uses the Google Sheets API to log transaction data. Follow these steps to set it up:

Create a Project in Google Cloud Console:

Go to the Google Cloud Console.
Create a new project or select an existing one.   
Enable Google Sheets API and Download Credentials:

Search for "Google Sheets API" and enable it for your project.
Create service account credentials (credentials.json) and download the file.
Configure config.py:

Open the config.py file in a text editor.
Replace SERVICE_ACCOUNT_FILE with the path to your downloaded credentials.json file.
4. Set Up Etherscan API Key
MerchNet uses the Etherscan API to fetch transaction data.

Obtain Etherscan API Key:

Sign up for an account on Etherscan.
Get your API key from your account settings.
Configure config.py:

Open the config.py file.
Replace ETHERSCAN_API_KEY with your Etherscan API key.
5. Run the Application
To start fetching and logging PYUSD transactions, execute the following command:

Bash

python merchnet.py
This script will fetch the latest transactions and log them into the Google Sheet specified in your configuration.

📜 License
This project is licensed under the MIT License. See the LICENSE file for more details.

🤝 Contributing
Contributions are welcome! Feel free to open issues and submit pull requests to help improve MerchNet.   

📞 Contact
GitHub: mredidy
Twitter: @mister_edidy
Discord: mredidy
Made with ❤️ for local businesses to make crypto payments easy and understandable.


Sources and related content

