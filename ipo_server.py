from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow requests from browser

@app.route("/ipo")
def get_ipo_data():
    url = "https://www.nseindia.com/api/ipo"
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept-Language": "en-US,en;q=0.9",
    }

    try:
        response = requests.get(url, headers=headers)
        data = response.json()

        # Extract only last 6 IPOs
        ipo_list = data["data"][-6:]

        return jsonify(ipo_list)

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
