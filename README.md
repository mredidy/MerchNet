# MerchNet

MerchNet is a real-time crypto payment insights tool designed for local businesses to easily track and understand on-chain PayPal USD (PYUSD) transactions. Built with simplicity and practicality in mind, MerchNet enables merchants to monitor live transactions, analyze customer and merchant behavior, and get real-time visibility into blockchain flows without needing technical expertise.

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1CKE-FuQhqF0sVVYuhINxsn8MpLw7h4Tb)

---

## 🚀 Problem Statement

As crypto adoption grows, local merchants face challenges in tracking and interpreting blockchain transactions. MerchNet addresses this gap by offering a no-code solution that provides:

- Real-time monitoring of PYUSD payments  
- Transaction metadata in a clean, human-readable format  
- Insights into regional transaction flows (opt-in)  
- Automatic logging and analysis in Google Sheets  

## 🧹 Project Overview

MerchNet uses Etherscan and Google Cloud's Blockchain Node Engine APIs to deliver valuable insights, including:

- **Real-time PYUSD transaction tracking**  
- **Known wallet labeling** (e.g., PayPal, exchanges, smart contracts)  
- **Etherscan links** for direct access to transaction details  
- **Google Sheets Sync** for easy tracking and analysis of transactions  
- **Geographic insight** into regional transaction flows (optional)  

## ✨ Features

- 🦾 **Live Etherscan API Integration:** Monitor real-time PYUSD transactions on the blockchain  
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

## 🏁 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/mredidy/MerchNet.git
cd MerchNet
```

### 2. Install Dependencies

Ensure you have Python 3.x installed, then install the required dependencies:

```bash
pip install -r requirements.txt
```

### 3. Set Up Google Sheets API

- Create a project in Google Cloud Console.  
- Enable Google Sheets API and download your `credentials.json` file.  
- Replace `SERVICE_ACCOUNT_FILE` in the `config.py` with the path to your credentials file.  

### 4. Set Up Etherscan API Key

- Sign up for an Etherscan account and obtain your API key.  
- Replace `ETHERSCAN_API_KEY` in the `config.py` with your API key.  

### 5. Run the Application

```bash
python merchnet.py
```

This will fetch the latest transactions and log them into the specified Google Sheet.

---

## 💻 Live Demo

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1CKE-FuQhqF0sVVYuhINxsn8MpLw7h4Tb)  
📊 [Open MerchNet in Google Colab](https://colab.research.google.com/drive/1CKE-FuQhqF0sVVYuhINxsn8MpLw7h4Tb)

---

## 📸 Screenshots & Walkthrough

### 🔁 MerchNet in Action (GIF Demo)
![MerchNet GIF Demo](https://github.com/mredidy/MerchNet/blob/main/assets/demo.gif)

### 📄 Google Sheets Format
![MerchNet Google Sheet](https://github.com/mredidy/MerchNet/blob/main/assets/google-sheets-format.png)

---

## 🗺 Roadmap

- [x] Real-time PYUSD transaction tracking via Etherscan
- [x] Google Sheets logging
- [x] Known wallet labeling
- [ ] Geographic transaction insights
- [ ] Integration with GCP Blockchain Node Engine
- [ ] Frontend dashboard

## 🤝 Contributing Guide

We welcome contributions from the community!

1. Fork the repository
2. Create a feature branch (`git checkout -b feature-name`)
3. Commit your changes (`git commit -m 'Add feature'`)
4. Push to the branch (`git push origin feature-name`)
5. Open a Pull Request

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/mredidy/MerchNet/blob/main/LICENSE) file for more details.

## 📞 Contact

- **GitHub:** [mredidy](https://github.com/mredidy)  
- **Twitter:** [@mister_edidy](https://twitter.com/mister_edidy)  
- **Discord:** `mredidy`  

---

Made with ❤️ for local businesses to make crypto payments easy and understandable.

