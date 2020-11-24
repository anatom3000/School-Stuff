# fichier utilisé seulemet pour tester les stats des équipes de le but de détermeiner des paris sur les scores réalistes

# RESULTAT AVEC 10000 MATCHS
# Max: 1050
# Moy: 159.2675
# Med: 160.0

import match

NB_MATCHS = 10000

max_score = 0
moy_score = 0
med_score = 0
scores = []
for i in range(NB_MATCHS):
    res = match.simulate("a", "b")
    scores.append(res["score"][0])
    scores.append(res["score"][1])
    max_score = max(max_score, res["score"][0])
    max_score = max(max_score, res["score"][1])

for i in scores:
    moy_score += i
moy_score /= NB_MATCHS * 2

scores.sort() 
mid = len(scores) // 2
med_score = (scores[mid] + scores[~mid]) / 2

print(f"Max: {max_score}")
print(f"Moy: {moy_score}")
print(f"Med: {med_score}")
