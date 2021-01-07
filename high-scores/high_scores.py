# Introduction
# Manage a game player's High Score list.

# Your task is to build a high-score component of the classic Frogger game, 
# one of the highest selling and addictive games of all time, 
# and a classic of the arcade era. 
# Your task is to write methods that return the highest score from the list, the last added score and the three highest scores.

def latest(scores):
    return scores[len(scores) - 1]

def personal_best(scores):
    scores.sort(reverse=True)
    return scores[0]

def personal_top_three(scores):
    scores.sort(reverse=True)
    topc = 3
    top = []
    if len(scores) < topc:
        topc = len(scores)

    for i in range(0, topc):
        top.append(scores[i])

    return top

# Test code
# lscore = [100, 0, 90, 30]
# lscore = [30, 70]
# print(latest(lscore))
# print(personal_best(lscore))
# print(personal_top_three(lscore))