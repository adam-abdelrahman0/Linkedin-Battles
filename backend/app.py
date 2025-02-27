from flask import Flask, request, jsonify
from flask_cors import CORS
from database import get_random_matchup, update_elo
import os

app = Flask(__name__)
CORS(app)  # Allows frontend requests

@app.route("/matchup", methods=["GET"])
def matchup():
    profiles = get_random_matchup()
    return jsonify(profiles)

@app.route("/vote", methods=["POST"])
def vote():
    data = request.json
    update_elo(data["winner_id"], data["loser_id"])
    return jsonify({"message": "Vote recorded!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)

