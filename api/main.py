
import os
from flask import Flask, request
import requests
from dotenv import load_dotenv

load_dotenv()

UNSPLASH_URL = "https://api.unsplash.com/photos/random/"
UNSPLASH_KEY = os.environ.get("UNSPLASH_KEY", "")
if not UNSPLASH_KEY:
    raise EnvironmentError("Please create .env local file and insert there UNSPLASH_KEY")

app = Flask(__name__)

@app.route("/new-image")
def new_route():
    word = request.args.get("query")
    headers = {
        "Accept-Version": "v1",
        "Authorization": f"Client-ID {UNSPLASH_KEY}"
        }
    params = {"query": word}
    response = requests.get(url=UNSPLASH_URL, headers=headers, params=params)
    data = response.json()
    return data


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)