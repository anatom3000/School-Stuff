def print_scoreboard(players, fields=None, limit=-1, fillchar='█'):
    # si fields n'est pas donné, alors le déduire du premier perso.
    if fields is None:
        fields = []
        for i in players[0]:
            fields.append(i)

    scoreboard = fillchar

    max_lenghts = {}
    for field in fields:
        max_lenghts[field] = len(field) + 2
        for player in players:
            max_lenghts[field] = max(max_lenghts[field], len(player[field]) + 2)

    for field in fields:
        scoreboard += field.center(max_lenghts[field] + 2) + fillchar

    scoreboard_width = len(scoreboard)

    scoreboard += '\n' + fillchar * scoreboard_width + '\n'

    i = 0
    for player in players:
        scoreboard += fillchar
        for field in fields:
            scoreboard += player[field].center(max_lenghts[field] + 2) + fillchar
        scoreboard += '\n'
        i += 1
        if i == limit:
            break

    scoreboard += fillchar * scoreboard_width

    return scoreboard
