file = "./input/input06.txt"

mat = [[0]*1000 for i in range(1000)]

with open("./input/input06.txt", "r") as f:
    for line in f:
        line_vec = line.split(" ")
        adj = 0
        if line_vec[0] != "toggle":
            adj = 1
        start = line_vec[1+adj]
        end = line_vec[3+adj]
        x0 = int(start.split(",")[0])
        y0 = int(start.split(",")[1])
        x1 = int(end.split(",")[0])
        y1 = int(end.split(",")[1])

        for i in range(x0,x1+1):
            for j in range(y0,y1+1):
                if line_vec[0] == "toggle":
                    mat[i][j] = 1 - mat[i][j]
                elif line_vec[1] == "on":
                    mat[i][j] = 1
                elif line_vec[1] == "off":
                    mat[i][j] = 0
                else:
                    print("no match")

total_on = sum([sum(i) for i in mat])
print(total_on)

# part 2

mat = [[0]*1000 for i in range(1000)]

with open("./input/input06.txt", "r") as f:
    for line in f:
        line_vec = line.split(" ")
        adj = 0
        if line_vec[0] != "toggle":
            adj = 1
        start = line_vec[1+adj]
        end = line_vec[3+adj]
        x0 = int(start.split(",")[0])
        y0 = int(start.split(",")[1])
        x1 = int(end.split(",")[0])
        y1 = int(end.split(",")[1])

        for i in range(x0,x1+1):
            for j in range(y0,y1+1):
                if line_vec[0] == "toggle":
                    mat[i][j] += 2
                elif line_vec[1] == "on":
                    mat[i][j] += 1
                elif line_vec[1] == "off":
                    mat[i][j] -= 1
                    if mat[i][j] < 0:
                        mat[i][j] = 0
                else:
                    print("no match")

total_on = sum([sum(i) for i in mat])
print(total_on)