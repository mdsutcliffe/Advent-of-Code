file = open("input/input10.txt", "r")
x = file.read().split("\n")
file.close()

boundary_limits = [len(x), len(x[0])]
start = [[ix, xi.find("S")] for ix, xi in enumerate(x) if xi.find("S") != -1][0]

valid_moves = {
  "-": [[0, 1], [0, -1]],
  "|": [[1, 0], [-1, 0]],
  "7": [[0, -1], [1, 0]],
  "J": [[0, -1], [-1, 0]],
  "L": [[-1, 0], [0, 1]],
  "F": [[0, 1], [1, 0]]
}

# PART 1
node_history = [start]
# Figure out where to go first
if x[start[0] + 1][start[1]] in "|JL":
  current_node = [start[0] + 1, start[1]]
elif x[start[0]][start[1] + 1] in "-7J":
  current_node = [start[0], start[1] + 1]
elif x[start[0] - 1][start[1]] in "|F7":
  current_node = [start[0] - 1, start[1]]
else:
  current_node = [start[0], start[1] - 1]
node_history.append(current_node)

while True:
  move_options = valid_moves.get(x[current_node[0]][current_node[1]])
  if [current_node[0] + move_options[0][0], current_node[1] + move_options[0][1]] not in node_history and \
          current_node[0] + move_options[0][0] in list(range(boundary_limits[0])) and \
          current_node[1] + move_options[0][1] in list(range(boundary_limits[1])):
    move = move_options[0]
  elif [current_node[0] + move_options[1][0], current_node[1] + move_options[1][1]] not in node_history and \
          current_node[0] + move_options[1][0] in list(range(boundary_limits[0])) and \
          current_node[1] + move_options[1][1] in list(range(boundary_limits[1])):
    move = move_options[1]
  else:
    break
  current_node = [current_node[0] + move[0], current_node[1] + move[1]]
  node_history.append(current_node)

steps_furthest = int(len(node_history) / 2)

print(steps_furthest)

# PART 2
x_vals = [i[1] for i in node_history]
y_vals = [-i[0] for i in node_history]


def shoelace(x, y):
  # https://en.wikipedia.org/wiki/Shoelace_formula
  a = 0
  for i in range(len(x)):
    # i - 1 works because it will go to end of list
    det = (x[i - 1] * y[i]) - (x[i] * y[i - 1])
    a += det
  return abs(a) / 2


area = int(shoelace(x_vals, y_vals) - len(node_history) / 2 + 1)

print(area)
