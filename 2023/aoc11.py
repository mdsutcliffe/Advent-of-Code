file = open("input/input11.txt", "r")
x = file.read().split("\n")
file.close()

x = [[*i] for i in x]


def find_empty(x):
  empty_rows = [all([xij == "." for xij in xi]) for xi in x]
  empty_columns = [all([xi[j] == "." for xi in x]) for j in range(len(x[0]))]

  empty_rows = [i for i, val in enumerate(empty_rows) if val]
  empty_columns = [i for i, val in enumerate(empty_columns) if val]
  return empty_rows, empty_columns


def find_galaxies(x):
  galaxies = []
  for i in range(len(x)):
    for j in range(len(x[i])):
      if x[i][j] == "#":
        galaxies.append([i, j])
  return galaxies


def calculate_distances(galaxies, scale_empty, empty_rows, empty_columns):
  d = []
  for i in range(len(galaxies) - 1):
    for j in range(i + 1, len(galaxies)):
      pair_rows = sorted([galaxies[i][0], galaxies[j][0]])
      pair_columns = sorted([galaxies[i][1], galaxies[j][1]])
      additional_rows = len(set(list(range(pair_rows[0], pair_rows[1]))).intersection(empty_rows)) * (scale_empty - 1)
      additional_columns = len(set(list(range(pair_columns[0], pair_columns[1]))).intersection(empty_columns)) * (scale_empty - 1)
      d.append(pair_rows[1] - pair_rows[0] +
               pair_columns[1] - pair_columns[0] +
               additional_rows + additional_columns)
  return d


def part1():
  empty_rows, empty_columns = find_empty(x)
  galaxies = find_galaxies(x)
  d = calculate_distances(galaxies, 2, empty_rows, empty_columns)
  return sum(d)


def part2():
  empty_rows, empty_columns = find_empty(x)
  galaxies = find_galaxies(x)
  d = calculate_distances(galaxies, 1_000_000, empty_rows, empty_columns)
  return sum(d)


print(part1())
print(part2())
