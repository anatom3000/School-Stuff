import csv
from random import randint

import match
import utils

# pour lire la base de données: https://docs.python.org/fr/3/library/csv.html

players = []
with open('Characters.csv', newline='') as f:
    reader = csv.DictReader(f, delimiter=';')
    for row in reader:
        players.append(row)

# on trouve toutes les équipes dans les joueurs
equipes = set()
for player in players:
    equipes.add(player["House"])
equipes = list(equipes)

# on ajoute de l'argent aux joueurs
for player in players:
    player["Money"] = 2
    player["ScoreBet"] = 0


for _ in range(10):
    answer = ""
    while answer != "o":
        answer = input("Commencer le match (o/n) ? ")
    
    print("Le match a commencé!")

    for player in players:
        if player["Money"] > 0:
            player["ScoreBet"] = randint(0, 320)
            player["Money"] -= 1
    
    res_match1 = match.simulate(equipes[0], equipes[1])
    res_match2 = match.simulate(equipes[2], equipes[3])
    winners = [res_match1["winner"], res_match2["winner"]]
    scores = {}
    for i, equipe in enumerate(equipes):
        if i < 2:
            scores[equipe] = res_match1["score"][i]
        else:
            scores[equipe] = res_match2["score"][i-2]

    nearest_score = 0
    for player in players:
        if player["House"] in winners:
            player["Money"] += 5
            if min(abs(nearest_score-scores[player["House"]]), \
                    abs(player["ScoreBet"]-scores[player["House"]]))\
                     != abs(nearest_score-scores[player["House"]]):
                nearest_score = player["ScoreBet"]

        if utils.isTrue(player["House"] in winners):
            if player["ScoreBet"] == nearest_score:
                player["Money"] += 30

    players = sorted(players, key=lambda  k: k["Money"])[::-1]

    if input("Voulez-vous afficher le scoreboard (o/n) ? ") == 'o':
        print(f"""{equipes[0]} - {equipes[1]}: {res_match1["score"][0]} - {res_match1["score"][1]}""")
        print(f"""{equipes[2]} - {equipes[3]}: {res_match2["score"][0]} - {res_match2["score"][1]}""")
        print(utils.print_scoreboard(players, fields=["Name", "House", "Money", "ScoreBet"], limit=10))




    

print(utils.print_scoreboard(players, fields=["Id", "Name", "Money"], limit=10)) 
