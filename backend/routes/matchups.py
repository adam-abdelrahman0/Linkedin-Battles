from flask import Blueprint, request, jsonify
from firebase_init import db
from utils.elo import calculate_elo
import random
from google.cloud.firestore_v1.base_query import FieldFilter

matchups_bp = Blueprint("matchups", __name__)

@matchups_bp.route("/matchup", methods=["GET"])
def create_matchup():
    users = [doc.to_dict() for doc in db.collection("users").stream()]
    user1, user2 = random.sample(users, 2)
    return jsonify({"user1": user1, "user2": user2})

# chat generated
def get_user_by_name(name):
    users_ref = db.collection("users")
    query = users_ref
    query = query.where(filter=FieldFilter("linkedin", "==", name))
    results = query.get()

    for doc in results:
        return doc  # Return Firestore document

    return None  # User not found

@matchups_bp.route("/submit", methods=["POST"])
def submit_matchup():
    data = request.json

    winner_name = data.get("winner_id", "")["linkedin"].strip()
    loser_name = data.get("loser_id", "")["linkedin"].strip()

    if not winner_name or not loser_name:
        return jsonify({"error": "Missing winner or loser name"}), 400

    winner_doc = get_user_by_name(winner_name)
    loser_doc = get_user_by_name(loser_name)

    if not winner_doc or not loser_doc:
        return jsonify({"error": "User not found"}), 404

    winner = winner_doc.to_dict()
    loser = loser_doc.to_dict()

    winner["elo"], loser["elo"] = calculate_elo(winner["elo"], loser["elo"], True)
    winner_ref = db.collection("users").document(winner_doc.id)
    loser_ref = db.collection("users").document(loser_doc.id)
    winner_ref.set(winner)
    loser_ref.set(loser)
    

    return jsonify({"message": "Matchup submitted successfully", "winner": winner, "loser": loser})