from flask import Flask, render_template
from flask_cors import CORS
from flask import jsonify
from flask import request
import requests

BINANCE_API_URL = "https://api.binance.com/api/v3/ticker/price"
app = Flask(__name__)
CORS(app)

tracked_pairs = {}  # {user_id: ["BTCUSDT", "ETHUSDT"]}

@app.route('/')
def index():
    return render_template("index.html")

TRACKED_PAIRS = ["BTCUSDT", "ETHUSDT", "BNBUSDT"]

@app.route("/track", methods=["POST"])
def track_pair():
    data = request.json
    user_id = data.get("user_id")
    pair = data.get("pair")

    if not user_id or not pair:
        return jsonify({"error": "user_id and pair required"}), 400

    if user_id not in tracked_pairs:
        tracked_pairs[user_id] = []

    if pair not in tracked_pairs[user_id]:
        tracked_pairs[user_id].append(pair)

    return jsonify({"message": "Pair added", "tracked": tracked_pairs[user_id]})

@app.route("/untrack", methods=["POST"])
def untrack_pair():
    data = request.json
    user_id = data.get("user_id")
    pair = data.get("pair")

    if not user_id or not pair:
        return jsonify({"error": "user_id and pair required"}), 400

    if user_id in tracked_pairs and pair in tracked_pairs[user_id]:
        tracked_pairs[user_id].remove(pair)

    return jsonify({"message": "Pair removed", "tracked": tracked_pairs.get(user_id, [])})


@app.route("/prices", methods=["GET"])
def get_prices():
    pair = request.args.get("pair")  # Получаем пару из запроса

    if not pair:
        return jsonify({"error": "pair required"}), 400

    try:
        response = requests.get(f"{BINANCE_API_URL}?symbol={pair}")
        data = response.json()

        if "price" in data:
            return jsonify({"symbol": pair, "price": data["price"]})
        else:
            return jsonify({"error": "Invalid pair"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)