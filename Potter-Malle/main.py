# coding: utf8

'''
Mini-projet "Harry se fait la malle"
Liste de fournitures scolaires
Auteur : David Landry
'''

fournitures_scolaires = [{'Nom' : 'Manuel scolaire', 'Poids' : 0.6, 'Mana' : 11},
                         {'Nom' : 'Baguette magique', 'Poids' : 0.085, 'Mana' : 120},
                         {'Nom' : 'Chaudron', 'Poids' : 2.7, 'Mana' : 2},
                         {'Nom' : 'Boîte de fioles', 'Poids' : 1.2, 'Mana' : 4},
                         {'Nom' : 'Téléscope', 'Poids' : 1.9, 'Mana' : 6},
                         {'Nom' : 'Balance de cuivre', 'Poids' : 1.2, 'Mana' : 3},
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
            if key(data[j]) < key(tab[mini]):
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
def partieABC(fournitures, max_poids, priorite=lambda x: x):

    fournitures = tri(fournitures, key=priorite, reverse=True)
    mis_dans_malle = []
    for f in fournitures:
        poids_total = 0
        for i in mis_dans_malle:
            poids_total += i["Poids"]
        if f['Poids'] + poids_total < max_poids:
            mis_dans_malle.append(f)

    return mis_dans_malle

partieABC(fournitures_scolaires, poids_maximal)                                # partie A
partieABC(fournitures_scolaires, poids_maximal, priorite=lambda x: x["Poids"]) # partie B
partieABC(fournitures_scolaires, poids_maximal, priorite=lambda x: x["Mana"] ) # partie C
