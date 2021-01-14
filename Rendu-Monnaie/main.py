#coding: utf-8

# CONSTANTES
BIG = 2**64


#On crée une fonction qui vérifie la caisse
def rendu_monnaie(monnaie, sysmoney=[200, 100, 50, 20, 10, 5, 2, 1], caisse=None):
    """
    rendu_monnaie permet de déterminer combien de pièces et de billets faut-il rendre.

    Entrées:
        monnaie (int): somme en euros à rendre.
        sysmoney (list<int>): système de monnaie utilisé. Chaque élément correspond à un type de billet/pièce.
        caisse (dict<int:int>): nombre de billets présents dans la caisse sous la forme {valeur_du_billet:nombre_de_billets}. Si pas utilisé la caisse sera remplie automatiquement d'un nombre très grand (voir constante BIG) pour chaque type de billet.
    Sorties:
        nb_billets (dict<int:int>): 
    """

    # si la caisse n'est pas utilisée, on la remplit au maximum
    if caisse is None:
        caisse = {i:BIG for i in sysmoney}
    sysmoney.sort(reverse=True)
    
    # on calcule la somme de la caisse
    somme = 0
    for billet, nb in caisse.items():
        somme += billet*nb
    # on verifie qu'il y a assez de monnaie dans la caisse. Si pas assez, on donne tout.
    if somme < monnaie:
        return caisse

    # on calcule combien il faut de billets
    nb_billets = {}
    for billet in sysmoney:
        resultat = divmod(monnaie, billet)
        if caisse[billet] > resultat[0]:
            nb_billets[billet] = resultat[0]
            monnaie = resultat[1]
        else:
            nb_billets[billet] = caisse[billet]
            monnaie -= caisse[billet]*billet
    

    return nb_billets

