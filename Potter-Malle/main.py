# coding: utf8

'''
Mini-projet "Harry se fait la malle"
Liste de fournitures scolaires
Auteur : David Landry
'''

def print_results(data):
    poids = 0
    for k, v in enumerate(data):
        print(f"### Objet n°{k+1} ###")
        print(f"Nom : {v['Nom']}")
        print(f"Poids : {v['Poids']}")
        print(f"Mana : {v['Mana']}")
        print()
        poids += v["Poids"]
    
    print(f"Poids total : {round(poids, 3)} kg.")
    
        


fournitures_scolaires = [
    {'Nom' : 'Manuel scolaire', 'Poids' : 0.55, 'Mana' : 11},
    {'Nom' : 'Baguette magique', 'Poids' : 0.085, 'Mana' : 120},
    {'Nom' : 'Chaudron', 'Poids' : 2.5, 'Mana' : 2},
    {'Nom' : 'Boîte de fioles', 'Poids' : 1.2, 'Mana' : 4},
    {'Nom' : 'Téléscope', 'Poids' : 1.9, 'Mana' : 6},
    {'Nom' : 'Balance de cuivre', 'Poids' : 1.3, 'Mana' : 3},
    {'Nom' : 'Robe de travail', 'Poids' : 0.5, 'Mana' : 8},
    {'Nom' : 'Chapeau pointu', 'Poids' : 0.7, 'Mana' : 9},
    {'Nom' : 'Gants', 'Poids' : 0.6, 'Mana' : 25},
    {'Nom' : 'Cape', 'Poids' : 1.1, 'Mana' : 13}
]


poids_maximal = 4

def tri(data, key=lambda x: x, reverse=False):
    for i in range(len(data) - 1):
        mini = i
        for j in range(i + 1, len(data)):
            if key(data[j]) < key(data[mini]):
                mini = j
        data[i], data[mini] = data[mini], data[i]
    return data


"""
Pseudo-code de partieABC:
DEFINIR partieABC(fournitures, max_poids):
    mis_dans_malle <- tableau vide
    POUR f DANS fournitures:
        poids_total <- 0
        POUR i DANS mis_dans_malle:
            poids_total <- poids_total + i["Poids"]
        FIN_POUR
        SI f['Poids'] + poids_total PLUS PETIT QUE max_poids:
            AJOUTER f A mis_dans_malle 
        FIN_SI
    FIN_POUR

    RETOURNER mis_dans_malle
FIN_DEFINIR
"""
def partieABC(fournitures, max_poids, priorite=None):

    if priorite is not None:
        fournitures = tri(fournitures, key=priorite, reverse=True)
    
    mis_dans_malle = []
    for f in fournitures:
        poids_total = 0
        for i in mis_dans_malle:
            poids_total += i["Poids"]
        if f['Poids'] + poids_total < max_poids:
            mis_dans_malle.append(f)

    return mis_dans_malle


print("Bienvenue dans notre app de rangement de malle.")
use_custom_fournitures = input("Voulez-vous entrer des fournitures personnalisées (y/n) ? ") in ['y', 'o', 'yes', 'oui']
if use_custom_fournitures:
    fournitures_scolaires = []
    nb_fournitures = int(input("Entrez le nombre d'objets que vous voulez proposer : "))
    for i in range(nb_fournitures):
        objet = {}
        print(f"### Objet n°{i+1} ###")
        objet["Nom"] = input("Nom : ")
        objet["Poids"] = float(input("Poids : "))
        objet["Mana"] = float(input("Mana : "))
        fournitures_scolaires.append(objet)


input_poids = input("Entrez le poids maximal (laisser blanc pour défaut) : ")
poids_maximal = int(input_poids) if input_poids != '' else poids_maximal

print("[a] Remplir n'importe comment")
print("[b] Remplir pour le plus lourd possible")
print("[c] Remplir pour le plus de mana possible")
mode = input("Entrez le mode de remplissage : ")
while mode.lower() not in ["a", "b", "c"]:
    print("Veuillez entrer une valeur valide (a/b/c)")
    mode = input("Entrez le mode de remplissage : ")


if mode.lower() == 'a':
    print_results(partieABC(fournitures_scolaires, poids_maximal))
elif mode.lower() == 'b':
    print_results(partieABC(fournitures_scolaires, poids_maximal, priorite=lambda x: x["Poids"]))
else:
    print_results(partieABC(fournitures_scolaires, poids_maximal, priorite=lambda x: x["Mana"]))

