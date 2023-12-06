import numpy as np

file = open("./input/input03.txt", "r")
x = file.read()
file.close()
x = list(x)

d = {
    "^": [0, 1],
    "v": [0, -1],
    ">": [1, 0],
    "<": [-1, 0]
}

i = [0, 0]
houses = []

for j in x:
    # print(j)
    # print(d[j])
    i = [(i[k] + d[j][k]) for k in range(2)]
    houses.append(i)
print(houses)
# print(set(houses))

z = [list(iz) for iz in set(tuple(iz) for iz in houses)]
print(len(z)+1)
    # i = map(sum, zip(i, d[j]))
    # print(i)

# z = [[0]*8192 for i in range(8192)]
# print(z)

for i in range(0, len(x), 2):
    print(i)

santa1_loc = [0, 0]
santa2_loc = [0, 0]
houses_santa1 = [santa1_loc]
houses_santa2 = [santa2_loc]

print(houses_santa1)
for i in range(len(x)):
    if i % 2 == 0:
        santa1_loc = [(santa1_loc[j] + d[x[i]][j]) for j in range(2)]
        houses_santa1.append(santa1_loc)
    else:
        santa2_loc = [(santa2_loc[j] + d[x[i]][j]) for j in range(2)]
        houses_santa2.append(santa2_loc)

set_santa1 = [list(i) for i in set(tuple(i) for i in houses_santa1)]
set_santa1 = [list(i) for i in set(tuple(i) for i in houses_santa1)]

houses_all = houses_santa1 + houses_santa2
set_all = [list(i) for i in set(tuple(i) for i in houses_all)]

print(len(set_all))