from collections import Counter

file = open("./input/input01.txt", "r")
x = file.read()
file.close()

y = Counter(x)
print(y["("] - y[")"])

# part 2
currentFloor = 0
for i, j in enumerate(x):
    if j == "(":
        currentFloor += 1
    elif j == ")":
        currentFloor -= 1
    if currentFloor <= -1:
        print(i+1)
        break
