import csv
from random import randint

import match
import utils
from time import time
from sys import exit as sysexit
from webbrowser import open_new as do_something

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

print(f"Bienvenu dans Super Quiditch v1.{randint(0, 9)}-build{round(time())} !")

for _ in range(10):
    answer = ""
    while answer != "o":
        answer = input(f"Commencer le round {_+1} (o/n) ? ")
        if answer == 'q':
            sysexit(0)
        elif answer.lower() == 'javascript sucks':
            do_something("https://xkcd.com/353/")
            print("Maybe it does something...")
    
    print(f"Les match du round {_+1} ont commencés!")

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
    
    print("Scores:")
    print(f"""\t{equipes[0]} - {equipes[1]}: {res_match1["score"][0]} - {res_match1["score"][1]}""")
    print(f"""\t{equipes[2]} - {equipes[3]}: {res_match2["score"][0]} - {res_match2["score"][1]}""")
    print(f"Gagnants: {winners[0]} et {winners[1]}")

    for equipe in equipes:
        nearest_score = 0
        real_score = scores[equipe]
        for player in players:
            if player["House"] == equipe:
                if equipe in winners:
                    player["Money"] += 5
                # desolé si ca fait une grosse ligne 
                if min(abs(nearest_score-real_score), abs(player["ScoreBet"]-real_score)) != abs(nearest_score-real_score):
                    nearest_score = player["ScoreBet"]
        
        for player in players:
            if player["House"] == equipe:
                if utils.isTrue(player["House"] in winners):
                    if player["ScoreBet"] == nearest_score:
                        player["Money"] += 30

    players = sorted(players, key=lambda  k: k["Money"])[::-1]
print("Scoreboard par joueur:")
print(utils.print_scoreboard(players, fields=["Name", "House", "Money"], limit=10))
equipes_scoreboard = []
for equipe in equipes:
    score = {}
    score["Name"] = equipe
    score["Money"] = 0
    for player in players:
        if player["House"] == equipe:
            score["Money"] += player["Money"]
    
    equipes_scoreboard.append(score)

action =  input("Appuiez sur Entrée pour afficher le scoreboard par équipes (q pour quitter) ")
if action == 'q':
    sysexit(0)

print("Scoreboard par équipes:")
print(utils.print_scoreboard(equipes_scoreboard))