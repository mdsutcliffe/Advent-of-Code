file = open("input/input01.txt", "r")
lines = file.read().split("\n")
file.close()

x = []
xi = 0
for line in lines:
    if line == "":
        x.append(xi)
        xi = 0
    else:
        xi += int(line)
x.sort(reverse=True)

# Part 1
print("Part 1: " + str(x[0]))

# Part 2
print("Part 2: " + str(sum(x[0:3])))
