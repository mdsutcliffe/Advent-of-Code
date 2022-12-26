file = open("input/input04.txt", "r")
lines = file.read().split("\n")[:-1]
file.close()

nSubsets = 0
nOverlaps = 0
for line in lines:
    x0 = line.split(",")[0].split("-")
    x1 = line.split(",")[1].split("-")

    x0 = [int(i) for i in x0]
    x1 = [int(i) for i in x1]

    set0 = set([j for j in range(x0[0], x0[1]+1)])
    set1 = set([j for j in range(x1[0], x1[1]+1)])

    if len(set0.intersection(set1)) > 0 or len(set1.intersection(set0)) > 0:
        nOverlaps += 1
        if len(set0.intersection(set1)) == len(set0) or len(set1.intersection(set0)) == len(set1):
            nSubsets += 1

print("Part 1: " + str(nSubsets))
print("Part 2: " + str(nOverlaps))
