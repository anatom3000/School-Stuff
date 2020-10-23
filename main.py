import csv
import pprint

import match
import utils

# pour lire la base de données: https://docs.python.org/fr/3/library/csv.html

players = []
with open('Characters.csv', newline='') as f:
    reader = csv.DictReader(f, delimiter=';')
    for row in reader:
        players.append(row)

print(utils.print_scoreboard(players, fields=["Id", "Name", "House", "Species"], limit=10))
