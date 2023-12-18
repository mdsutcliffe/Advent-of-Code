file = open("input/input18.txt", "r")
x = [[j for j in i.split()] for i in file.read().split("\n")]
file.close()


def shoelace(x, y):
  # https://en.wikipedia.org/wiki/Shoelace_formula
  a = 0
  for i in range(len(x)):
    # i - 1 works because it will go to end of list
    det = (x[i - 1] * y[i]) - (x[i] * y[i - 1])
    a += det
  return abs(a) / 2


def dig_trench(direction, length, direction_dict):
  row_vals = []
  col_vals = []
  row_i = col_i = 0
  for i_step, _ in enumerate(direction):
    row_vals.append(row_i)
    col_vals.append(col_i)
    di, dj = direction_dict.get(direction[i_step])
    di *= length[i_step]
    dj *= length[i_step]
    row_i += di
    col_i += dj
  return row_vals, col_vals


def part1():
  direction_dict = {"R": [0, 1], "L": [0, -1], "D": [1, 0], "U": [-1, 0]}
  direction = [i[0] for i in x]
  length = [int(i[1]) for i in x]
  r, c = dig_trench(direction, length, direction_dict)

  outline = sum(length)
  area = int(outline / 2 + shoelace(r, c) + 1)
  return area


def part2():
  direction_dict = {"0": [0, 1], "2": [0, -1], "1": [1, 0], "3": [-1, 0]}
  direction = [i[2][-2] for i in x]
  length = [int(i[2][2:7], 16) for i in x]
  r, c = dig_trench(direction, length, direction_dict)

  outline = sum(length)
  area = int(outline / 2 + shoelace(r, c) + 1)
  return area

print(part1())
print(part2())
