# 📁 MerchNet Updater

**MerchNet Updater** is a lightweight Python microservice built with Flask and Google Cloud that updates a Google Sheet in real-time with the latest PayPal USD (PYUSD) token transfer data from Ethereum, using BigQuery public datasets.

> 🔁 This service powers the **MerchNet Insights** dashboard — providing local businesses and analysts with a no-code, live crypto payment monitoring tool.

---

## 🚀 Features

- Fetches the latest 100 PYUSD transactions from Ethereum using BigQuery
- Formats and writes data to a Google Sheet
- Adds rich formatting, Etherscan links, and a live dashboard title
- Easily deployable via Google Cloud Run or any containerized environment

---

## 📦 Project Structure

```
merchnet-updater/
├── main.py             # Flask app entrypoint
├── updater.py          # Logic to fetch and write PYUSD data to Sheets
├── requirements.txt    # Python dependencies
├── Dockerfile          # Container build definition
└── README.md           # You're here
```

---

## 🔧 Setup

### 1. Clone the Repo

```bash
git clone https://github.com/mredidy/merchnet-updater.git
cd merchnet-updater
```

### 2. Add Your Service Account

Save your Google service account key file as:

```
MerchNet-Insights.json
```

Ensure this account has access to:
- Google Sheets & Drive APIs
- BigQuery public dataset: `bigquery-public-data.crypto_ethereum.token_transfers`

---

## 🧪 Local Testing

```bash
pip install -r requirements.txt
python main.py
```

Open [http://localhost:8080](http://localhost:8080) to trigger a sheet update.

---

## 🐳 Docker Usage

### Build Image

```bash
docker build -t merchnet-updater .
```

### Run Container

```bash
docker run -p 8080:8080 -v $(pwd)/MerchNet-Insights.json:/app/MerchNet-Insights.json merchnet-updater
```

---

## ☁️ Deployment (GCP Cloud Run)

1. Push your container to Google Artifact Registry or Docker Hub
2. Deploy with Cloud Run
3. Make sure to mount the service account or use Workload Identity

---

## 📜 License

MIT © [mredidy](https://github.com/mredidy)

---

## 🔗 Related Projects

- [MerchNet Dashboard](https://github.com/mredidy/merchnet) — Live crypto payments dashboard
- [Google BigQuery Ethereum Public Dataset](https://console.cloud.google.com/marketplace/details/bigquery-public-data/crypto-ethereum)

---

## 👦 Follow the Journey

**Twitter:** [@mister_edidy](https://twitter.com/mister_edidy)  
**GitHub:** [mredidy](https://github.com/mredidy)

