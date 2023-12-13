file = open("input/input13.txt", "r")
x = file.read().split("\n\n")
file.close()

x = [i.split("\n") for i in x]


def find_reflection(x, smudges):
  for i_row, _ in enumerate(x[:-1]):
    errors_total = 0
    errors_i = sum([x[i_row][i] != x[i_row + 1][i] for i, _ in enumerate(x[i_row])])
    if errors_i <= smudges:
      errors_total += errors_i
      offset_row = 1
      flag = True
      while i_row - offset_row >= 0 and i_row + offset_row + 1 < len(x):
        if x[i_row - offset_row] != x[i_row + offset_row + 1]:
          if errors_total >= smudges:
            flag = False
            break
          else:
            errors_total += sum([x[i_row - offset_row][i] != x[i_row + offset_row + 1][i] for i, _ in enumerate(x[i_row])])
        offset_row += 1
      if flag and errors_total == smudges:
        return i_row + 1
  return 0


def part1():
  points = []
  for x_i in x:
    points.append(find_reflection(x_i, 0) * 100)
    x_i_transpose = ["".join(i) for i in list(map(list, zip(*x_i)))]
    points.append(find_reflection(x_i_transpose, 0))
  return sum(points)


def part2():
  points = []
  for x_i in x:
    points.append(find_reflection(x_i, 1) * 100)
    x_i_t = ["".join(i) for i in list(map(list, zip(*x_i)))]
    points.append(find_reflection(x_i_t, 1))
  return sum(points)


print(part1())
print(part2())
