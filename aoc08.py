file = open("input/input08_test", "r")
lines = file.read().split("\n")[:-1]
file.close()

x = [[int(i) for i in line] for line in lines]
xt = [[x[j][i] for j in range(len(x))] for i in range(len(x[0]))]

# ~~~~~ PART 1 ~~~~~
visible = [[1 for j in range(len(row))] for row in x]
# left and right
for i in range(1, len(x)-1):
    row = x[i]
    for j in range(1, len(row)-1):
        visible[i][j] = 0
        # left
        visible_left = True
        for k in range(0, j):
            if row[k] >= row[j]:
                visible_left = False
                break
        # right
        visible_right = True
        for k in range(j+1, len(row)):
            if row[k] >= row[j]:
                visible_right = False
                break
        if visible_left or visible_right:
            visible[i][j] = 1

# top and bottom
for i in range(1, len(xt)-1):
    col = xt[i]
    for j in range(1, len(col)-1):
        if visible[j][i]:
            continue
        visible[j][i] = 0
        # top
        visible_top = True
        for k in range(0, j):
            if col[k] >= col[j]:
                visible_top = False
                break
        # bottom
        visible_bottom = True
        for k in range(j + 1, len(col)):
            if col[k] >= col[j]:
                visible_bottom = False
                break
        if visible_top or visible_bottom:
            visible[j][i] = 1
# print(sum([sum(i) for i in visible]))

# ~~~~~ PART 2 ~~~~~
scenic_score = [[0 for j in range(len(row))] for row in x]
for i in range(len(x)):
    row = x[i]
    for j in range(len(row)):
        col = xt[j]
        i = 2
        j = 2
        for ii in range(j, 0-1, -1):
            if row[ii]
        break
    break