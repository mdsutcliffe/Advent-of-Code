file = open("input/input14.txt", "r")
x = file.read().split("\n")
file.close()


def slide_north(x):
  x = ["".join(i) for i in list(map(list, zip(*x)))]
  while any([".O" in i for i in x]):
    x = [i.replace(".O", "O.") for i in x]
  x = ["".join(i) for i in list(map(list, zip(*x)))]
  return x


def run_cycle(x):
  # north
  x = ["".join(i) for i in list(map(list, zip(*x)))]
  while any([".O" in i for i in x]):
    x = [i.replace(".O", "O.") for i in x]
  # west
  x = ["".join(i) for i in list(map(list, zip(*x)))]
  while any([".O" in i for i in x]):
    x = [i.replace(".O", "O.") for i in x]
  # south
  x = ["".join(i)[::-1] for i in list(map(list, zip(*x)))]
  while any([".O" in i for i in x]):
    x = [i.replace(".O", "O.") for i in x]
  x = [i[::-1] for i in x]
  # east
  x = ["".join(i)[::-1] for i in list(map(list, zip(*x)))]
  while any([".O" in i for i in x]):
    x = [i.replace(".O", "O.") for i in x]
  x = [i[::-1] for i in x]
  return x


def calculate_load(x):
  rocks = []
  for i_x, x_i in enumerate([list(i) for i in x]):
    for j_x, x_ij in enumerate(x_i):
      if x_ij == "O":
        rocks.append((i_x, j_x))
  return sum([len(x) - i[0] for i in rocks])


def part1(x):
  x = slide_north(x)
  return calculate_load(x)


def part2(x, total_cycles):
  previous_cycles = [(0, x.copy())]
  for cycle_i in range(1, total_cycles + 1):
    x = run_cycle(x)
    # Check to see if we've seen this arrangement before
    add_flag = True
    for previous_cycle_i in previous_cycles:
      if all([x[i] == previous_cycle_i[1][i] for i, _ in enumerate(x)]):
        add_flag = False
        break
    if add_flag:
      previous_cycles.append((cycle_i, x))
    else:
      break

  cycle_length = cycle_i - previous_cycle_i[0]
  n_additional_cycles = (total_cycles - cycle_i) % cycle_length

  # remainder to get to 1e9
  for i_additional in range(n_additional_cycles):
    x = run_cycle(x)

  return calculate_load(x)

print(part1(x))
print(part2(x, 1_000_000_000))
