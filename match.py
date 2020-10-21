import random


def simulate(equipe1, equipe2):
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
