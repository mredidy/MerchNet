# MerchNet

MerchNet is a real-time crypto payment insights platform focused on tracking PayPal USD (PYUSD) transactions across Ethereum and Solana. It is designed for local businesses and developers who need visibility into stablecoin adoption and movement.

## 🌐 Live Demo
Check out the live dashboard here: [Google Sheets MerchNet Insights](https://docs.google.com/spreadsheets/d/1ETOF3XHbWNZGlQ8TCWmJd22f-tqJGANc)

---

## 🚀 Features

- 🔎 Real-time monitoring of PYUSD transactions on Ethereum using GCP Blockchain RPC
- 🧠 Uses GCP’s free access to computationally expensive methods like `debug_traceTransaction`
- 📊 Historical analytics powered by Google BigQuery for Ethereum and Solana
- 🌍 No-code dashboard using Google Sheets
- 🔗 Clickable Etherscan links for easy traceability
- 🧠 Known wallet identification & metadata tagging
- 💵 USD-equivalent formatting for readability

---

## 🔧 Tech Stack

- **Google Cloud Blockchain Node Engine** – Real-time Ethereum mainnet RPC access
- **BigQuery** – Historical blockchain data analysis
- **gspread / gspread-formatting** – Export and style data in Google Sheets
- **Google Colab** – Code execution environment
- **Etherscan API** – Transaction metadata and links

---

## 📦 Setup Instructions

### 1. Clone the Repo
```bash
git clone https://github.com/mredidy/merchnet.git
cd merchnet
```

### 2. Setup Credentials
- Upload your `MerchNet-Insights.json` (GCP service account key)
- Store in Google Secret Manager as `merchnet-service-account`

### 3. Configure Parameters
Set these in the script or as environment variables:
- GCP Project ID: `red-parity-456515-t4`
- Sheet Name: `MerchNet Insights`
- Folder ID: `1ETOF3XHbWNZGlQ8TCWmJd22f-tqJGANc`
- Ethereum Contract: `0x6c3ea9036406852006290770bedfcaba0e23a0e8`

### 4. Run the Notebook
- Open the Colab notebook and execute all cells.

---

## 📟️ Demo Video
👉 [Coming Soon - Stay Tuned!]

---

## 🧪 Example Use Cases

- Small businesses accepting PYUSD payments
- Analysts tracking stablecoin activity in DeFi
- Developers building smart dashboards with no-code tools

---

## 📜 License
This project is licensed under the MIT License.

---

## 🙌 Acknowledgements
- StackUp x Google Cloud Bounty
- Paxos + PYUSD APIs
- GCP Web3 RPC team
- Ethereum & Solana public datasets

---

## 🧠 Author
**mredidy**  
GitHub: [@mredidy](https://github.com/mredidy)  
Twitter: [@mister_edidy](https://twitter.com/mister_edidy)  
Discord: `mredidy`

---

## 🔮 Roadmap
- [x] Live Ethereum RPC connection via GCP
- [x] Real-time PYUSD fetch & Etherscan linking
- [ ] Integrate `trace_transaction` to trace fund flows
- [ ] Add support for smart contract call decoding
- [ ] Merge Solana and Ethereum into unified insights layer
- [ ] Add mobile-friendly frontend with Glide or React

