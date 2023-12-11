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


def expand_universe(x, scale, empty_rows, empty_columns):
  x_expanded = x.copy()
  offset_i = 0
  for i in range(len(x_expanded)):
    if i in empty_rows:
      x_expanded = x_expanded[:(i + offset_i)] + \
                   [["."] * len(x_expanded[i])] * (scale - 1) + \
                   x_expanded[(i + offset_i):]
      offset_i += (scale - 1)
  for i in range(len(x_expanded)):
    offset_j = 0
    for j in range(len(x_expanded[i])):
      if j in empty_columns:
        x_expanded[i] = x_expanded[i][:(j + offset_j)] + \
                        ["."] * (scale - 1) + \
                        x_expanded[i][(j + offset_j):]
        offset_j += (scale - 1)
  return x_expanded


def calculate_distances(galaxies):
  d = []
  for i in range(len(galaxies) - 1):
    for j in range(i + 1, len(galaxies)):
      d.append(abs(galaxies[j][0] - galaxies[i][0]) + abs(galaxies[j][1] - galaxies[i][1]))
  return d

def part1(x):
  empty_rows, empty_columns = find_empty(x)
  x = expand_universe(x, 2, empty_rows, empty_columns)
  galaxies = find_galaxies(x)
  d = calculate_distances(galaxies)
  return sum(d)

print(part1(x))

# PART 2
def calculate_distances_expand(galaxies, scale, empty_rows, empty_columns):
  d = []
  for i in range(len(galaxies) - 1):
    for j in range(i + 1, len(galaxies)):
      rows = sorted([galaxies[i][0], galaxies[j][0]])
      columns = sorted([galaxies[i][1], galaxies[j][1]])
      d_rows = len(set(list(range(rows[0], rows[1]))).intersection(empty_rows)) * (scale - 1)
      d_columns = len(set(list(range(columns[0], columns[1]))).intersection(empty_columns)) * (scale - 1)
      d.append(rows[1] - rows[0] + columns[1] - columns[0] + d_rows + d_columns)
  return d


def part2(x):
  empty_rows, empty_columns = find_empty(x)
  # DON'T ACTUALLY EXPAND THE UNIVERSE
  galaxies = find_galaxies(x)
  d = calculate_distances_expand(galaxies, 1_000_000, empty_rows, empty_columns)
  return sum(d)


print(part2(x))
