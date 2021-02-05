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

def sort_mais_pas_celui_de_la_bibliotheque_standard(data, key=lambda x: x, reverse=False):
    for i in range(len(data) - 1):
        mini = i
        for j in range(i + 1, len(data)):
            if key(data[j]) < key(tab[mini]):
                mini = j
        data[i], data[mini] = data[mini], data[i]
    return data

# partie A - n'importe comment

def partieA(fourn, max_poids):

    mis_dans_malle = []
    for f in fourn:
        poids_total = 0
        for i in mis_dans_malle:
            poids_total += i["Poids"]
        if f['Poids'] + poids_total < max_poids:
            mis_dans_malle.append(f)

    return mis_dans_malle


# partie B - plus lourd possible

def partieB(fourn, max_poids):

    fourn = sort_mais_pas_celui_de_la_bibliotheque_standard(fourn, key=lambda x: x["Poids"], reverse=True)
    mis_dans_malle = []
    for f in fourn:
        poids_total = 0
        for i in mis_dans_malle:
            poids_total += i["Poids"]
        if f['Poids'] + poids_total < max_poids:
            mis_dans_malle.append(f)

    return mis_dans_malle



# partie C - plus de mana possible

def partieC(fourn, max_poids):

    fourn = sort_mais_pas_celui_de_la_bibliotheque_standard(fourn, key=lambda x: x["Mana"], reverse=True)
    mis_dans_malle = []
    for f in fourn:
        poids_total = 0
        for i in mis_dans_malle:
            poids_total += i["Poids"]
        if f['Poids'] + poids_total < max_poids:
            mis_dans_malle.append(f)

    return mis_dans_malle

print(partieA(fournitures_scolaires, poids_maximal))
print()
print(partieB(fournitures_scolaires, poids_maximal))
print()
print(partieC(fournitures_scolaires, poids_maximal))
