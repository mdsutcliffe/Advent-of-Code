import itertools
file = open("input/input22_test.txt", "r")
x = [[[int(k) for k in j.split(",")] for j in i.split("~")] for i in file.read().split("\n")]
# x = file.read().split("\n")
# x = [j for i in file.read().split("\n") for j in i.split("~")]
file.close()

def get_bottom_edge(coordinates):
  # return [list(range(coordinates[0][0], coordinates[1][0]+1)),
  #         list(range(coordinates[0][1], coordinates[1][1]+1)),
  #         coordinates[0][2]]
  return list(itertools.product(list(range(coordinates[0][0], coordinates[1][0]+1)),
                                list(range(coordinates[0][1], coordinates[1][1]+1))))

print(get_bottom_edge(x[0]))



def argsort(l):
  return sorted(range(len(l)), key=l.__getitem__)


x = [x[i] for i in argsort([min([i[0][2], i[1][2]]) for i in x])]

xi = x[0]