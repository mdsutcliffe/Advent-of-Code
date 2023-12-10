file = open("input/input09.txt", "r")
x = file.read().split("\n")
file.close()

x = [[int(i) for i in j.split()] for j in x]


def get_sequence(x):
  if all([x_i == 0 for x_i in x]):
    return [x]
  dx = [x[i+1] - x[i] for i in range(len(x)-1)]
  return [x] + get_sequence(dx)


def part1():
  history_sum = 0
  for x_i in x:
    history_sum += sum([s_i[-1] for s_i in get_sequence(x_i)])
  return history_sum

print(part1())


def recursive_subtract(x):
  if len(x) == 0:
    return 0
  return x[0] - recursive_subtract(x[1:])


def part2():
  history_sum = 0
  for x_i in x:
    s = [s_i[0] for s_i in get_sequence(x_i)]
    sx = recursive_subtract(s)
    history_sum += sx
  return history_sum


print(part1())
print(part2())
