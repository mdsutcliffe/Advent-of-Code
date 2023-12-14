file = open("input/input14.txt", "r")
x = file.read().split("\n")
file.close()


def part1(x):
  x = [list(i) for i in x.copy()]
  cubes =[]
  rocks = []
  for i_x, x_i in enumerate([list(i) for i in x]):
    for j_x, x_ij in enumerate(x_i):
      if x_ij == "#":
        cubes.append((i_x, j_x))
      if x_ij == "O":
        rocks.append((i_x, j_x))
  # move rocks
  for i_rock, _ in enumerate(rocks):
    if rocks[i_rock][0] == 0:
      continue
    while (rocks[i_rock][0] - 1, rocks[i_rock][1]) not in rocks and \
      (rocks[i_rock][0] - 1, rocks[i_rock][1]) not in cubes and \
            rocks[i_rock][0] > 0:
      rocks[i_rock] = (rocks[i_rock][0] - 1, rocks[i_rock][1])
  return sum([len(x) - i[0] for i in rocks])


def part2(x):
  def run_cycle(x):
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

  previous_cycles = [(0, x.copy())]
  for cycle_i in range(1, 1_000_000_000 + 1):
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

  def calculate_load(x):
    rocks = []
    for i_x, x_i in enumerate([list(i) for i in x]):
      for j_x, x_ij in enumerate(x_i):
        if x_ij == "O":
          rocks.append((i_x, j_x))
    return sum([len(x) - i[0] for i in rocks])

  cycle_length = cycle_i - previous_cycle_i[0]
  n_additional_cycles = (1_000_000_000 - cycle_i) % cycle_length

  # remainder to get to 1e9
  for i_additional in range(n_additional_cycles):
    x = run_cycle(x)

  return calculate_load(x)

print(part1(x))
print(part2(x))
