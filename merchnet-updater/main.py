from flask import Flask
from updater import update_sheet

app = Flask(__name__)

@app.route('/')
def home():
    return '📡 MerchNet Updater is live!'

@app.route('/update', methods=['GET'])
def trigger_update():
    result = update_sheet()
    return result

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
