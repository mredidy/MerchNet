# MerchNet

**Seamless Transactions, Infinite Possibilities — Challenge 1 Submission**

MerchNet is a real-time crypto payment insights tool designed for local businesses. Built with simplicity, clarity, and real-world utility in mind, it helps merchants monitor, analyze, and understand on-chain activity involving PayPal USD (PYUSD) using public blockchain APIs, with an emphasis on Google Cloud's Blockchain Node Engine.

---

## 🚀 Problem Statement

Crypto adoption is growing, but local merchants struggle to track and make sense of blockchain transactions. There's no easy, no-code tool tailored for them to:

- Monitor PYUSD payments
- Understand customer and merchant behavior
- Get real-time visibility into on-chain flows

**MerchNet** fills this gap by delivering real-time transaction feeds and merchant-centric insights using public APIs and on-chain data.

---

## 🧩 Project Overview

MerchNet leverages Etherscan and GCP Blockchain RPC APIs to:

- Track live PYUSD token transactions
- Identify known wallets (e.g., exchanges, smart contracts)
- Display transaction metadata in a clean, human-readable format
- Export and update transaction data automatically in Google Sheets
- Provide merchants with transparency and geographic insight without technical complexity

---

## ✨ Features

- 🧾 **Live Etherscan API Integration**: Monitor new PYUSD transactions in real-time
- 🔗 **Etherscan Links**: Direct access to transaction details on-chain
- 🧠 **Known Wallet Labeling**: Contextual metadata for addresses (e.g. PayPal, exchanges)
- 📊 **Google Sheets Sync**: Auto-logging to Google Sheets for analysis
- 🌍 **Geographic Insight (opt-in)**: View regional transaction flows (optional, privacy-respecting)
- 🧪 **Built with public data**: 100% open-source and reproducible

---

## 🛠 Tech Stack

- **Python** (Google Colab for development & runtime)
- **Etherscan API** (for blockchain data)
- **Google Sheets API** (for auto-logging and reporting)
- **Google Cloud Blockchain RPC** (planned in Challenge 2)

---

## 🔄 How It Works

1. **Fetch Transactions**: Uses Etherscan API to fetch recent PYUSD token transfers
2. **Process Data**: Extracts sender, receiver, value, timestamp, and labels known wallets
3. **Update Sheet**: Logs each transaction with metadata and a direct Etherscan link into Google Sheets
4. **(Optional)**: Associates transactions with country/region data (planned post-Challenge 1)

---

## 📦 Setup Instructions

1. Clone the repo:

```bash
git clone https://github.com/your-username/merchnet.git
```

2. Open the Colab notebook:

```
MerchNet/main.ipynb
```

3. Upload your `Google Sheets API` credentials (`MerchNet-Google-Sheets-API.json`)

4. Run the notebook cells in order to start fetching data.

---

## 📈 Usage Guide

- Transactions will be fetched in intervals (configurable)

- Google Sheets will auto-populate with the following columns:

  - Timestamp
  - From Address (with label)
  - To Address (with label)
  - PYUSD Amount
  - Tx Hash
  - Etherscan Link

- You can open your Google Sheet anytime to view or analyze the data in real time

---

## 🧑‍⚖️ License

This project is licensed under the **MIT License**. See the `LICENSE` file for details.

---

## 🙌 Credits

- Built for the **StackUp Bounty Challenge: Seamless Transactions, Infinite Possibilities**
- Inspired by tools like Dune Analytics, Nansen, and Chainalysis, but made radically simpler for local businesses

---

## 📹 Demo Video

👉 [Link to video will be here once it's uploaded]

---

## 📌 Future Scope (Challenge 2)

- GCP Blockchain RPC integration for tracing and computational analysis
- Merchant behavior heatmaps & dashboards
- Web UI for simplified access
- Filtering and categorization by merchant type or region

---

**Built by Mr. Edidy with ❤️ for the community.**

