import networkx as nx

file = open("input/input17_test.txt", "r")
x = [[int(i) for i in x_i] for x_i in file.read().split("\n")]
file.close()

direction = {(-1, 0): "N", (1, 0): "S", (0, -1): "W", (0, 1): "E"}


def node_id(i, j):
  return i * len(x[0]) + j


def node_coordinates(id):
  i = int(id / len(x[0]))
  j = int(id % len(x[0]))
  return i, j


def get_direction(node_id_from, node_id_to):
  i_from, j_from = node_coordinates(node_id_from)
  i_to, j_to = node_coordinates(node_id_to)
  return direction.get((i_to - i_from, j_to - j_from))


g = []
for i, _ in enumerate(x):
  for j, _ in enumerate(x[i]):
    node_from = node_id(i, j)
    if j > 0:
      node_to = node_id(i, j - 1)
      g.append([node_from, node_to, x[i][j - 1]])
    if j < (len(x[i]) - 1):
      node_to = node_id(i, j + 1)
      g.append([node_from, node_to, x[i][j + 1]])
    if i > 0:
      node_to = node_id(i - 1, j)
      g.append([node_from, node_to, x[i - 1][j]])
    if i < (len(x) - 1):
      node_to = node_id(i + 1, j)
      g.append([node_from, node_to, x[i + 1][j]])

G = nx.DiGraph()
[G.add_edge(i[0], i[1], weight=i[2]) for i in g]

nx.shortest_path_length(G, source=0, target=168, weight="weight")

paths = nx.shortest_simple_paths(G, source=0, target=len(x)*len(x[0])-1, weight="weight")

for i_path, path_i in enumerate(paths):
  if i_path % 1000 == 0:
    print(i_path)
  if i_path < 15_000:
    continue
  d_count = 0
  flag = True
  for i in range(0, len(path_i) - 2):
    d_from = get_direction(path_i[i], path_i[i+1])
    d_to = get_direction(path_i[i+1], path_i[i+2])
    if (d_from == "N" and d_to == "S") or \
            (d_from == "S" and d_to == "N") or \
            (d_from == "E" and d_to == "W") or \
            (d_from == "W" and d_to == "E"):
      flag = False
      break
    if d_from == d_to:
      d_count += 1
    else:
      d_count = 0
    if d_count > 3:
      flag = False
      break
  if flag:
    print(nx.path_weight(G, path_i, "weight"))
    break
  # break

x2 = [list(i) for i in x]
for i in path_i:
  ii, jj = node_coordinates(i)
  x2[ii][jj] = 0


for i in x2:
  print(i)

