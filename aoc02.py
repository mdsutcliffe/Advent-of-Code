file = open("input/input02.txt", "r")
lines = file.read().split("\n")[:-1]
file.close()

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

wins = ["A Y", "B Z", "C X"]
draws = ["A X", "B Y", "C Z"]
score1 = 0
for line in lines:
    score1 += score_choice[line[2]]
    if line in wins:
        score1 += score_outcome["win"]
    elif line in draws:
        score1 += score_outcome["draw"]
    else:
        score1 += score_outcome["lose"]
print("Part 1: " + str(score1))

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
score2 = 0
for line in lines:
    if line[2] == "X":
        # need to lose
        score2 += score_choice[to_lose[line[0]]]
        score2 += score_outcome["lose"]
    elif line[2] == "Y":
        score2 += score_choice[to_draw[line[0]]]
        score2 += score_outcome["draw"]
    else:
        # need to win
        score2 += score_choice[to_win[line[0]]]
        score2 += score_outcome["win"]
print("Part 2: " + str(score2))