from flask import Blueprint, request, jsonify
from firebase_init import db

users_bp = Blueprint("users", __name__)

@users_bp.route("/add", methods=["POST"])
def add_user():
    data = request.json
    user_ref = db.collection("users").document()
    user_ref.set({
        "name": data["name"],
        "linkedin": data["linkedin"],
        "elo": 1200
    })
    return jsonify({"success": True, "user_id": user_ref.id})

@users_bp.route("/all", methods=["GET"])
def get_users():
    users = db.collection("users").stream()
    return jsonify([{"id": user.id, **user.to_dict()} for user in users])
