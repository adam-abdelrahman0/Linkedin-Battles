from flask import Blueprint, request, jsonify
from firebase_init import db
from utils.elo import calculate_elo

matchups_bp = Blueprint("matchups", __name__)

@matchups_bp.route("/submit", methods=["POST"])
def submit_matchup():
    data = request.json
    user1_id, user2_id, winner_id = data["user1"], data["user2"], data["winner"]

    user1_ref = db.collection("users").document(user1_id)
    user2_ref = db.collection("users").document(user2_id)

    user1 = user1_ref.get().to_dict()
    user2 = user2_ref.get().to_dict()

    if not user1 or not user2:
        return jsonify({"error": "User not found"}), 404

    new_elo1, new_elo2 = calculate_elo(user1["elo"], user2["elo"], winner_id == user1_id)

    user1_ref.update({"elo": new_elo1})
    user2_ref.update({"elo": new_elo2})

    return jsonify({"success": True, "new_elo": {user1_id: new_elo1, user2_id: new_elo2}})
