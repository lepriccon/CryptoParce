from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="178.150.235.69", port=5000)