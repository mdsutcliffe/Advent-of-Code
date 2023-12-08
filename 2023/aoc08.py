import numpy as np
import re

file = open("input/input08.txt", "r")
x = file.read().split("\n\n")
file.close()

instructions = x[0].replace("L", "0").replace("R", "1")


def build_dict(x):
  d = dict()
  for i in x[1].split("\n"):
    node, left, right = re.search("^([A-Z0-9]+) = \\(([A-Z0-9]+), ([A-Z0-9]+)\\)", i).groups()
    d.update({(node, (left, right))})
  return d


def part1():
  current_node = "AAA"
  i = 0
  total_steps = 0
  while current_node != "ZZZ":
    current_node = d.get(current_node)[int(instructions[i])]
    i += 1
    if i == len(instructions):
      i = 0
    total_steps += 1
  return total_steps


def part2():
  current_nodes = [i for i in list(d.keys()) if i[-1] == "A"]
  z_index = [[] for i in current_nodes]
  i = 0
  total_steps = 0

  while any([len(z_index_i) < 2 for z_index_i in z_index]):
    current_nodes = [d.get(cn_i)[int(instructions[i])] for cn_i in current_nodes]
    i += 1
    if i == len(instructions):
      i = 0
    total_steps += 1
    for i_cn, cn_i in enumerate(current_nodes):
      if cn_i[-1] == "Z":
        z_index[i_cn].append(total_steps)
  cycle_lengths = [i[1] - i[0] for i in z_index]
  return np.lcm.reduce(cycle_lengths)


d = build_dict(x)
print(part1())
print(part2())