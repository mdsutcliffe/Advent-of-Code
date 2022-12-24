file = open("input/input07_test.txt", "r")
file.readline()  # root directory, not needed
lines = file.read().split("\n")
file.close()

x = ["/"]
level = 0
loc = [0]

i = 0
while True:
    if lines[i][:4] == "$ cd" and lines[i][5:] != "..":
        print("CDIN " + lines[i])
        x.append(lines[i][5:])
        i += 1
        level += 1
        loc.append(0)
    if lines[i] == "$ cd ..":
        print("CDUP " + lines[i])
        x.pop()
        i += 1
        level -= 1
        loc.pop()
        loc[level] += 1
    if lines[i] == "$ ls":
        print("LIST " + lines[i])
        i += 1
        while lines[i][0] != "$":
            if lines[i][:3] == "dir":
                print("DIRC " + lines[i])
                i += 1
            else:
                print("FILE " + lines[i])
                i += 1
            if lines[i] == "":
                break
            if i >= 15:
                break
    if lines[i] == "":
        break
    if i >= 15:
        break
print(x)
print(level)
print(loc)

i = 0

