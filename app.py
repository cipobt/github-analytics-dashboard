from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the GitHub Analytics Dashboard!"

if __name__ == "__main__":
    app.run(debug=True)

import requests
from flask import request, jsonify

ACCESS_TOKEN = "your_personal_access_token"
GITHUB_API_URL = "https://api.github.com"

@app.route('/fetch-profile', methods=['GET'])
def fetch_profile():
    """Fetch a GitHub user's profile information."""
    username = request.args.get('username')
    if not username:
        return jsonify({"error": "Username is required"}), 400

    headers = {"Authorization": f"token {ACCESS_TOKEN}"}
    response = requests.get(f"{GITHUB_API_URL}/users/{username}", headers=headers)

    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": response.json()}), response.status_code

