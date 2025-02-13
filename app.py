from flask import Flask, render_template, jsonify
from flask_cors import CORS

import utilities.request_methods

BINANCE_API_URL = "https://api.binance.com/api/v3/ticker/price"

binance_prices = {}
app = Flask(__name__)
CORS(app)

@app.route("/api/prices")
def api_prices():
    return jsonify(utilities.request_methods.get_binance_prices())

@app.route('/')
def index():
    return render_template('index.html', binance_prices=binance_prices)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)