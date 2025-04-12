# 📋 MerchNet – Crypto Payment Insights for Local Businesses

MerchNet is a lightweight tool that helps local businesses make sense of cryptocurrency payment activity in their area — starting with **PYUSD** transactions. By tapping into public blockchain APIs and visualizing data through Google Sheets, MerchNet gives businesses actionable insights about where, when, and how crypto is being used.

---

## 🔍 What Problem Does MerchNet Solve?

Cryptocurrency adoption is growing fast, but local merchants often struggle with:
- **Understanding real demand** in their region
- **Tracking crypto transaction trends**
- **Making informed decisions** about accepting stablecoins like PYUSD

MerchNet solves this by turning blockchain data into easy-to-read tables, helping merchants:
- See recent PYUSD transactions nearby
- Identify hotspots of crypto usage
- Analyze volume, time patterns, and wallet behavior

---

## 🚀 How It Works

1. MerchNet fetches **on-chain data** using the [Blockscout API](https://blockscout.com/) for Ethereum-compatible chains.
2. Transactions are filtered by:
   - Stablecoin: PYUSD
   - Geo relevance (e.g., US-based or filtered by known wallets)
3. The results are automatically exported to **Google Sheets**, which allows easy sharing, filtering, and analysis.

---

## 🎥 Demo Video

📻 **[Watch the demo](#)**  
*Link your video here once uploaded to YouTube or Drive*

---

## 🛠️ How To Use

### 🔧 Requirements
- A **Google account**
- Access to **Google Colab**
- A **Google Cloud service account key** with Sheets and Drive API enabled

### 🧪 Setup Instructions

1. **Clone the repository**  
```bash
git clone https://github.com/your-username/merchnet.git
```

2. **Open the Colab notebook**  
   - [Click here to run in Google Colab](#) *(Insert notebook link)*

3. **Provide your Google Sheets API credentials**  
   - Upload your `.json` service account key file

4. **Run the cells step-by-step** to:
   - Fetch transactions
   - Process and filter data
   - Export the data to Google Sheets (shared folder or personal)

---

## 📄 License

This project is licensed under the **MIT License**.  
See `LICENSE` file for details.

---

## 📬 Contact

Created by **@mister_edidy**  
On X (Twitter): [@mister_edidy](https://twitter.com/mister_edidy)  
Available on Discord too: *mredidy*

