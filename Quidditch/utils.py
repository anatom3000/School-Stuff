def print_scoreboard(players, fields=None, limit=-1, fillchar='█'):
    """
    Cette fonction génère un scoreboard qu'on peut alors afficher dans la console

    Entrées:
        players: liste de dictionnaires qui contient tous les joueurs à afficher
        fields: liste de propriétés sur les joueurs à afficher. si omit on  affiche toute les propriétés des joueurs
        limit: entier qui determine le nombre de joueurs à afficher
        fillchar: caractère permettant de remplir la structure du tableau
    Sortie:
        Retourne le scoreboard qu'on peut alors afficher (si on veut, je ne force personne)
    """

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
            max_lenghts[field] = max(max_lenghts[field], len(str(player[field])) + 2)

    for field in fields:
        scoreboard += field.center(max_lenghts[field] + 2) + fillchar

    scoreboard_width = len(scoreboard)

    scoreboard += '\n' + fillchar * scoreboard_width + '\n'

    i = 0
    for player in players:
        scoreboard += fillchar
        for field in fields:
            scoreboard += str(player[field]).center(max_lenghts[field] + 2) + fillchar
        scoreboard += '\n'
        i += 1
        if i == limit:
            break

    scoreboard += fillchar * scoreboard_width

    return scoreboard

def isTrue(b):
    """
    Cette fonction détermine si b est vrai et retourne True si b est vrai et False si b est faux.
    """
    if b == True:
        return True
    else:
        return False
        
