file = open("input/input21_test.txt", "r")
x = [list(i) for i in file.read().split("\n")]
file.close()

d = dict()
for i_x, x_i in enumerate(x):
  for j_xi, x_ij in enumerate(x_i):
    if x_ij in ".S":
      s = 0
      if i_x > 0 and x[i_x - 1][j_xi] in ".S":
        s += 1
      if i_x < len(x) - 1 and x[i_x + 1][j_xi] in ".S":
        s += 1
      if j_xi > 0 and x[i_x][j_xi - 1] in ".S":
        s += 1
      if j_xi < len(x_i) - 1 and x[i_x][j_xi + 1] in ".S":
        s += 1
      d.update({(i_x, j_xi)})
