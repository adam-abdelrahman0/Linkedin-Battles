def calculate_elo(elo1, elo2, is_winner):
    K = 32  # Elo constant
    expected1 = 1 / (1 + 10**((elo2 - elo1) / 400))
    expected2 = 1 / (1 + 10**((elo1 - elo2) / 400))

    if (is_winner):
        new_elo1 = elo1 + K * (1 - expected1)
        new_elo2 = elo2 + K * (0 - expected2)
    else:
        new_elo1 = elo1 + K * (0 - expected1)
        new_elo2 = elo2 + K * (1 - expected2)

    return round(new_elo1), round(new_elo2)
