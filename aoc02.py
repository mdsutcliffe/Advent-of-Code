f = open("input02.txt","r")

score_choice = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

score_outcome = {
    "lose": 0,
    "draw": 3,
    "win": 6
}

# wins = ["A Y", "B Z", "C X"]
# draws = ["A X","B Y","C Z"]
# score = 0
# for i in f:
#     i = i[0:3]
#     score += score_choice[i[2]]
#     if i in wins:
#         score += score_outcome["win"]
#     elif i in draws:
#         score += score_outcome["draw"]
#     else:
#         score += score_outcome["lose"]
# print(score)

to_lose = {
    "A": "Z",
    "B": "X",
    "C": "Y"
}
to_draw = {
    "A": "X",
    "B": "Y",
    "C": "Z"
}
to_win = {
    "A": "Y",
    "B": "Z",
    "C": "X"
}
score = 0
for i in f:
    if i[2] == "X":
        # need to lose
        score += score_choice[to_lose[i[0]]]
        score += score_outcome["lose"]
    elif i[2] == "Y":
        score += score_choice[to_draw[i[0]]]
        score += score_outcome["draw"]
    else:
        # need to win
        score += score_choice[to_win[i[0]]]
        score += score_outcome["win"]
print(score)