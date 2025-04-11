# MerchNet 🚀💸  
**Cryptocurrency Payment Insights for Local Businesses**

MerchNet is an easy-to-use, decentralized Web3 analytics tool designed to help local businesses make sense of cryptocurrency payments. By analyzing PayPal USD (PYUSD) transactions, it delivers valuable insights such as payment trends, hotspots, and transaction patterns, all based on real-world geolocation data. Whether you're a merchant or a community enthusiast, MerchNet enables informed decisions on crypto adoption.

---

## 🌍 What It Does

- **Track Crypto Payments**: Visualize the usage of PYUSD near your business.
- **Geolocation Insights**: Discover local hotspots for crypto transactions.
- **Empower Local Economies**: Make decisions based on real-time and historical data.
- **Easy Integration**: No coding or technical skills required; export results to Google Sheets.

---

## ⚙️ How It Works

1. **Data Sources**  
   - Google Cloud Blockchain RPC for Ethereum and Holesky testnet
   - OpenStreetMap for geolocation
   - BigQuery for Ethereum public datasets

2. **Processing**  
   - Fetchs PYUSD transaction data using RPC methods like `debug_traceTransaction`
   - Matches transaction metadata to geographical locations using OpenStreetMap
   - Analyzes and aggregates data based on time, location, and payment trends

3. **Output**  
   - Displayed directly in a Google Colab notebook
   - Exportable to Google Sheets for further analysis
   - Visualize in heatmaps or charts for easy interpretation

---

## 🚀 How to Use MerchNet

1. Clone or fork this repository.
2. Open the notebook `MerchNet_Colab_Notebook.ipynb` on [Google Colab](https://colab.research.google.com/).
3. Run the steps in the notebook to retrieve live data.
4. View insights directly or export to Google Sheets.

---

## 📽 Demo Video

👉 [Watch the Demo Video Here](#)  
The demo video will guide you through setting up, running the tool, and analyzing the insights provided by MerchNet.

---

## 📜 License

This project is licensed under the MIT License.

---

## 🔗 Contact

Built by [@mister_edidy](https://x.com/mister_edidy)  
Hackathon Discord: `mister_edidy#xxxx`
