import random


def simulate(equipe1, equipe2):
    """
    Cette fonction simule le match de 2 équipes (equipe1, equipe2)
    Entrées:
        equipe1 et equipe2: le noms des 2 equipes
    Sortie:
        Retourne un dictionnaire qui contient:
            1) les scores des 2 equipes
            2) la durée du match
            3) le nom du gagnant du match
    """
    score = [0, 0]
    match_continues = True
    time = 0
    while match_continues:
        if random.randint(1, 3) == 1:
            score[0] += 10
        if random.randint(1, 50) == 1:
            score[0] += 150
            match_continues = False
            continue

        if random.randint(1, 3) == 1:
            score[1] += 10
        if random.randint(1, 50) == 1:
            score[1] += 150
            match_continues = False
            continue
        time += 5

    winner = equipe1 if max(score) == score[0] else equipe2

    return {"score": score, "time": time, "winner": winner}
