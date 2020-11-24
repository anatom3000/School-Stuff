# on importe les modules necessaires
import csv

from random import randint
from time import time
from sys import exit as sysexit
from webbrowser import open_new as do_something

# on importe les differentes parties du programme
import match
import utils

# on commence par extraire les personnages de leur fichier d'origine
players = []
with open('Characters.csv', newline='') as f:
    reader = csv.DictReader(f, delimiter=';')
    for row in reader:
        players.append(row)

# on trouve toutes les équipes dans les joueurs
# pour cela on utilise les sets: cela permet d'importer toutes les équipes
# sans se soucier des doublons
equipes = set()
for player in players:
    equipes.add(player["House"])
equipes = list(equipes)

# on ajoute de l'argent aux joueurs
for player in players:
    player["Money"] = 2
    player["ScoreBet"] = 0

# on affiche un message de bienvenue 
# notons que personne n'a compris où vient cette ligne, mais quand on la supprime, le programme ne marche plus
print(f"Bienvenu dans Super Quiditch v1.{randint(0, 9)}-build{round(time())} !")

print()


# boucle des rounds
for _ in range(10):
    # on demande si on veut commencer le match
    # tant que l'utilisateur ne répond pas 'o', on redemande
    answer = ""
    while answer != "o":
        answer = input(f"Commencer le round {_+1} (o/n) ? ")
        if answer == 'q':
            sysexit(0)
        elif answer.lower() == 'javascript sucks':
            do_something("https://xkcd.com/353/")
            print("Maybe it does something...")
    
    # on annonce les matchs du round actuel ont commencés
    print(f"Les matchs du round {_+1} ont commencés!")

    # pour tous les joueurs, on verifie si il peuvent parier (assez d'argent) et on leur fait parier un score sur leur équipe
    for player in players:
        if player["Money"] > 0:
            player["ScoreBet"] = randint(0, 320)
            player["Money"] -= 1
    
    # on simule les matchs 
    res_match1 = match.simulate(equipes[0], equipes[1])
    res_match2 = match.simulate(equipes[2], equipes[3])

    # on definit une variable qui contient les Gagnants des 2 matchs
    winners = [res_match1["winner"], res_match2["winner"]]
    # on crée un dictionnaire qui permettra d'acceder au score d'une équipe en donnant son nom
    scores = {}
    for i, equipe in enumerate(equipes):
        if i < 2:
            scores[equipe] = res_match1["score"][i]
        else:
            scores[equipe] = res_match2["score"][i-2]
    
    # on affiche les scores des differentes equipes
    print("Scores:")
    print(f"""\t{equipes[0]} - {equipes[1]}: {res_match1["score"][0]} - {res_match1["score"][1]}""")
    print(f"""\t{equipes[2]} - {equipes[3]}: {res_match2["score"][0]} - {res_match2["score"][1]}""")
    
    # on affiche les gagnants
    print(f"Gagnants: {winners[0]} et {winners[1]}")
    print()

    # on determine, pour chaque equipe,  le joueur qui a le score parié le plus proche du score réel
    for equipe in equipes:
        nearest_score = 0
        # on crée une variable qui contiendra le vrai score (pour des raisons de lisibilité)
        real_score = scores[equipe]
        # pour chaque joueur de l'equipe, on lui ajoute 5€ si son equipe a gagnée et on determine le score parié le plus proche (mais sans relier le score le plus proche au joueur qui l'a parié)
        for player in players:
            if player["House"] == equipe:
                if equipe in winners:
                    player["Money"] += 5
                # desolé si ca fait une grosse ligne 
                if min(abs(nearest_score-real_score), abs(player["ScoreBet"]-real_score)) != abs(nearest_score-real_score):
                    nearest_score = player["ScoreBet"]
        
        # on relie le score le plus proche à son parieur
        for player in players:
            if player["House"] == equipe:
                if utils.isTrue(player["House"] in winners):
                    if player["ScoreBet"] == nearest_score:
                        player["Money"] += 30

    # on trie les joueurs du plus haut score au plus bas score
    players = sorted(players, key=lambda  k: k["Money"])[::-1]

# on affiche le scoreboard par joueur
print("Scoreboard par joueur:")
print(utils.print_scoreboard(players, fields=["Name", "House", "Money"], limit=10))

# on marque une pause pour que l'utilisateur puisse lire le scoreboard par joueur sans prise de tete
input("Appuiez sur Entrée pour afficher le scoreboard par équipes (q pour quitter) ")

# on genère le scoreboard par équipes: le score d'une equipe est le total de tous les scores des joueurs de cette équipe
equipes_scoreboard = []
for equipe in equipes:
    score = {}
    score["House"] = equipe
    score["Money"] = 0
    for player in players:
        if player["House"] == equipe:
            score["Money"] += player["Money"]
    
    equipes_scoreboard.append(score)

# on trie les équipes du plus haut score au plus bas score
equipes_scoreboard = sorted(equipes_scoreboard, key=lambda  k: k["Money"])[::-1]

# on affiche le scoreboard par équipe
print("Scoreboard par équipes:")
print(utils.print_scoreboard(equipes_scoreboard))

# fin :) j'espère que vous avez apprecié la lecture de ce code