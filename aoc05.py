f = open("input/input05.txt", "r")
y = []
line = ""
while True:
    line_previous = line
    line = f.readline()[:-1]
    if len(line) == 0:
        stacks = line_previous
        break
    else:
        z = [line[i] for i in range(len(line)) if i % 4 == 1]
        y.append(z)
stacks = [stacks[i] for i in range(len(stacks)) if i % 4 == 1]
stacks = [[] for i in range(len(stacks))]

# put boxes in their place
for i in range(len(y)-2,-1,-1):
    line = y[i]
    for j in range(len(line)):
        if line[j] != " ":
            stacks[j].append(line[j])
# part 1
# for line in f:
#     line = line[:-1].split(" ")
#     for i in range(int(line[1])):
#         stacks[int(line[5])-1].append(stacks[int(line[3])-1].pop())
# print("".join([i[-1] for i in stacks]))


# part 2
for line in f:
    line = line[:-1].split(" ")
    to_add = stacks[int(line[3]) - 1][-int(line[1]):]
    [stacks[int(line[5])-1].append(i) for i in to_add]
    [stacks[int(line[3])-1].pop() for i in to_add]
print(stacks)
print("".join([i[-1] for i in stacks]))
f.close()
