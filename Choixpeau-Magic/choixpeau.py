import csv
from math import sqrt

def dist(x, y):
    """
    Calcule la distance algébrique entre 2 personnages en utilisant ces caracteristiques.
    Entrées:
        x, y (dict): personnages
    Sortie:
        Distance entre les 2 personnages

    """
    a = y["Ambition"] - x["Ambition"]
    c = y["Courage"] - x["Courage"]
    g = y["Good"] - x["Good"]
    i = y["Intelligence"] - x["Intelligence"]
    return sqrt(a**2 + c**2 + g**2 + i**2)

def knn(db, char, k):
    """
    Renvoie les k plus proches voisins.
    Entrées:
        db (list<dict>): base de données de Poudlard
        char (dict): personnage pour qui renvoyer les kppv
        k (int): nombre de plus proches voisins
    Sortie:
        Les k plus proches voisins
    """
    return sorted(db, key=lambda x: dist(x, char))[:k]

# importation de Characters.csv
characters = []
with open('Characters.csv', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f, delimiter=';')
    for row in reader:
        characters.append(row)

# importation de Characters_chars.csv
characters_chars = []
with open('Characters_chars.csv', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f, delimiter=';')
    for row in reader:
        characters_chars.append(row)

# fusion des 2 tables
for cc in characters_chars:
    for i in ["Ambition", "Courage", "Good", "Intelligence"]:
        cc[i] = int(cc[i])
characters_unified = []
for c in characters:
    for cc in characters_chars:
        if c["Name"] == cc["Name"]:
            characters_unified.append({**c, **cc})

# liste des perso. a tester
profiles_cdc = [
    {"Courage":9, "Ambition":2, "Intelligence":8, "Good":9},
    {"Courage":9, "Ambition":4, "Intelligence":8, "Good":9},
    {"Courage":3, "Ambition":8, "Intelligence":6, "Good":3},
    {"Courage":2, "Ambition":3, "Intelligence":7, "Good":8}
]

# IHM. Simple. Efficace. Ergonomique.
# L'IHM. Réinventée.
k = 5
for p in profiles_cdc:
    print("Affichage des k(=5) plus proches voisins de", p)
    res = knn(characters_unified, p, k)
    for c in res:
        for i in ["Name", "House"]:
            print(i, ":", c[i], end=' ; ')
        print()
    print('-'*20)


quit = False
# IHM avancée pour tester des valeurs personalisées
while not quit:
    print("Options avancées pour entrer des valeurs personnalisées")
    print("-"*20)
    print('Entrez les caracteristiques')
    perso = {}
    for i in ["Ambition", "Courage", "Good", "Intelligence"]:
        good_try = False
        while not good_try:
            try:
                perso[i] = int(input(i+': '))
                good_try = True
            except ValueError:
                print("Veuillez entrer une valeur valide !")
    good_k = False
    while not good_k:
        try:
            k = eval(input("k = "))
            good_k = True
        except ValueError:
            print("Veuillez entrer une valeur valide !")
    
    res = knn(characters_unified, perso, k)
    print()
    for c in res:
        for i in ["Name", "House", "Ambition", "Courage", "Good", "Intelligence"]:
            print(i, ":", c[i], end=' ; ')
        print()
    
    quit = input("Voulez vous quitter ? ").lower() in ["oui", "yes", "o", "y"]