file = open("input/input15.txt", "r")
x = file.read().split(",")
file.close()

def hash(x):
  current_value = 0
  for x_i in x:
    current_value += ord(x_i)
    current_value *= 17
    current_value %= 256
  return current_value


def part1():
  values = []
  for x_i in x:
    values.append(hash(x_i))
  return sum(values)


def part2():
  boxes = [[] for i in range(256)]

  for x_i in x:
    operation = x_i[max([x_i.find("="), x_i.find("-")])]
    label, focal_length = x_i.split(operation)
    box = hash(label)

    label_ind = [i for i, j in enumerate(boxes[box]) if j[0] == label]
    if operation == "-":
      if len(label_ind) > 0:
        boxes[box].pop(label_ind[0])
    else:
      if len(label_ind) > 0:
        boxes[box][label_ind[0]] = (label, focal_length)
      else:
        boxes[box].append((label, focal_length))

  focusing_power = []
  for i_b, b_i in enumerate(boxes):
    for i_l, l_i in enumerate(b_i):
      focusing_power.append((i_b + 1) * (i_l + 1) * int(l_i[1]))

  return sum(focusing_power)

print(part1())
print(part2())
