import math

# input_file = "input/input06_test.txt"
input_file = "input/input06.txt"
with open(input_file, "r") as f:
  x = f.read().split("\n")

times = [int(i) for i in x[0].split()[1:]]
distances = [int(i) for i in x[1].split()[1:]]


def quadratic_formula(a, b, c):
  return (-1 * b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a), \
         (-1 * b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)


def n_ways_to_win(time, distance):
  winning_times = sorted(quadratic_formula(-1, time, -distance))
  min_time = math.floor(winning_times[0])+1
  max_time = math.ceil(winning_times[1])-1
  return max_time - min_time + 1


def part1():
  y = 1
  for race in range(len(times)):
    y = y * n_ways_to_win(times[race], distances[race])
  return y


def part2():
  time_cat = int("".join([str(i) for i in times]))
  distance_cat = int("".join([str(i) for i in distances]))
  return n_ways_to_win(time_cat, distance_cat)



# def part1():
#   y = 1
#   for race in range(len(times)):
#     wins = [i for i in range(times[race]) if (times[race] - i) * i > distances[race]]
#     y = y * len(wins)
#   return y
#


# def part2():
#   time_all = int("".join([str(i) for i in times]))
#   distance_all = int("".join([str(i) for i in distances]))
#   wins = [i for i in range(time_all) if (time_all - i) * i > distance_all]
#   return len(wins)


print(part1())

print(part2())
