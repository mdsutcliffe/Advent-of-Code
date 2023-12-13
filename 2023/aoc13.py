file = open("input/input13.txt", "r")
x = file.read().split("\n\n")
file.close()

x = [i.split("\n") for i in x]


def find_reflection(x):
  for i_r, r_i in enumerate(x[:-1]):
    if r_i == x[i_r + 1]:
      j = 1
      flag = True
      while i_r - j >= 0 and i_r + j + 1 < len(x):
        if x[i_r - j] != x[i_r + j + 1]:
          flag = False
          break
        j += 1
      if flag:
        return (i_r + 1)
  return 0


def part1():
  points = []
  for x_i in x:
    points.append(find_reflection(x_i) * 100)
    x_i_t = ["".join(i) for i in list(map(list, zip(*x_i)))]
    points.append(find_reflection(x_i_t))
  return sum(points)


def find_reflection_smudge(x):
  for i_r, r_i in enumerate(x[:-1]):
    n_errors = 0
    if sum([x[i_r][i] != x[i_r + 1][i] for i in range(len(x[0]))]) <= 1:
      n_errors += sum([x[i_r][i] != x[i_r + 1][i] for i in range(len(x[0]))])
      j = 1
      flag = True
      while i_r - j >= 0 and i_r + j + 1 < len(x):
        if x[i_r - j] != x[i_r + j + 1]:
          if n_errors >= 1:
            flag = False
            break
          else:
            n_errors += sum([x[i_r - j][i] != x[i_r + j + 1][i] for i in range(len(x[0]))])
        j += 1
      if flag and n_errors == 1:
        return (i_r + 1)
  return 0


def part2():
  points = []
  for x_i in x:
    points.append(find_reflection_smudge(x_i) * 100)
    x_i_t = ["".join(i) for i in list(map(list, zip(*x_i)))]
    points.append(find_reflection_smudge(x_i_t))
  return sum(points)


print(part1())
print(part2())
