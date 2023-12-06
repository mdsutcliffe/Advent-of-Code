file = open("./input/input02.txt", "r")
x = file.read().split("\n")
file.close()

x.pop()
total_surface_area = 0
for i, j in enumerate(x):
    # print(x[i])
    y = x[i].split("x")
    y = [int(k) for k in y]
    y.sort()
    sa = 3*y[0]*y[1] + 2*y[0]*y[2] + 2*y[1]*y[2]
    total_surface_area += sa

print(total_surface_area)

total_length_ribbon = 0
for i in x:
    y = i.split("x")
    y = [int(j) for j in y]
    y.sort()
    total_length_ribbon += 2*y[0] + 2*y[1] + y[0]*y[1]*y[2]

print(total_length_ribbon)