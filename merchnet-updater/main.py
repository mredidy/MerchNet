import os
from flask import Flask
from updater import update_sheet  # assuming your logic is in updater.py

app = Flask(__name__)

@app.route("/")
def hello():
    return "👋 MerchNet Updater is live!"

@app.route("/cron")
def run_cron():
    try:
        result = update_sheet()
        return result
    except Exception as e:
        return f"❌ Cron error: {str(e)}", 500

@app.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
