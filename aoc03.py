file = open("input/input03.txt", "r")
lines = file.read().split("\n")[:-1]
file.close()

lower_case = [chr(i) for i in range(ord("a"), ord("z") + 1)]
upper_case = [chr(i) for i in range(ord("A"), ord("Z") + 1)]
letters = lower_case + upper_case

score = 0
for line in lines:
    i0 = line[:len(line) // 2]
    i1 = line[len(line) // 2:]
    intersect = list(set(i0) & set(i1))[0]
    score += letters.index(intersect) + 1
print("Part 1: " + str(score))

score = 0
for i0 in range(0, len(lines), 3):
    line0 = lines[i0]
    line1 = lines[i0+1]
    line2 = lines[i0+2]
    common = list(set(line0) & set(line1) & set(line2))[0]
    score += letters.index(common) + 1
print("Part 2: " + str(score))
