# O(N) time and O(N) space
def tournamentWinner(competitions, results):
    teamScores = dict()

    # Adding up the scores for the winning teams throughout the tournament
    for idx, teams in enumerate(competitions):
        winner = teams[0] if results[idx] == 1 else teams[1]
        teamScores[winner] = teamScores.get(winner, 0) + 3

    # Searching for the tournament winner
    tourWinner = ""
    maxScore = 0

    for winner, score in teamScores.items():
        if score > maxScore:
            tourWinner = winner
            maxScore = score

    return tourWinner
