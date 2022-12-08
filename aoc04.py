f = open("input04.txt", "r")

nSubsets = 0
for i in f:
    i = i[:-1] # remove newline
    x = i.split(",")
    x0 = x[0].split("-")
    x1 = x[1].split("-")
    y0 = set([j for j in range(int(x0[0]), int(x0[1])+1)])
    y1 = set([j for j in range(int(x1[0]), int(x1[1])+1)])

    if len(y0.intersection(y1)) > 0 or len(y1.intersection(y0)) > 0:
        print("True")
        nSubsets += 1
    else:
        print(False)
print(nSubsets)
