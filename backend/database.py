import firebase_admin
from firebase_admin import credentials, firestore
import random
from backend.utils.elo import calculate_elo
from firebase_init import db


def get_random_matchup():
    users = [doc.to_dict() for doc in db.collection("users").stream()]
    return random.sample(users, 2)

def update_elo(winner_id, loser_id):
    winner_ref = db.collection("users").document(winner_id)
    loser_ref = db.collection("users").document(loser_id)

    winner = winner_ref.get().to_dict()
    loser = loser_ref.get().to_dict()

    winner["elo"], loser["elo"] = calculate_elo(winner["elo"], loser["elo"])

    winner_ref.set(winner)
    loser_ref.set(loser)
