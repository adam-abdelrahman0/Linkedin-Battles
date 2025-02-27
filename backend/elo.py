def calculate_elo(winner_elo, loser_elo, k=32):
    expected_winner = 1 / (1 + 10**((loser_elo - winner_elo) / 400))
    expected_loser = 1 - expected_winner

    new_winner_elo = winner_elo + k * (1 - expected_winner)
    new_loser_elo = loser_elo + k * (0 - expected_loser)

    return round(new_winner_elo), round(new_loser_elo)
