# file = open("input05_test.txt", "r")
file = open("input05.txt", "r")
x = file.read().split("\n\n")
file.close()

seeds = [int(i) for i in x[0][x[0].find(":") + 1:].split()]
maps = [i.split("\n")[1:] for i in x[1:]]
maps = [[[int(map_iii) for map_iii in map_ii.split()] for map_ii in map_i] for map_i in maps]


def part1():
  locations = seeds.copy()
  for i_seed, seed_i in enumerate(locations):
    for i_map, map_i in enumerate(maps):
      for ii_map, map_ii in enumerate(map_i):
        if locations[i_seed] >= map_ii[1] and locations[i_seed] <= (map_ii[1] + map_ii[2]):
          locations[i_seed] = map_ii[0] + locations[i_seed] - map_ii[1]
          break
  return min(locations)


print(part1())

seeds_range = [seed_i for i, seed_i in enumerate(seeds) if i % 2 == 1]
seeds = [seed_i for i, seed_i in enumerate(seeds) if i % 2 == 0]


def part2():
  i = 0
  while True:
    j = i
    for i_map, map_i in reversed(list(enumerate(maps))):
      for ii_map, map_ii in enumerate(map_i):
        if j >= map_ii[0] and j < (map_ii[0] + map_ii[2]):
          j = map_ii[1] + j - map_ii[0]
          break
    for i_seed, seed_i in enumerate(seeds):
      if j >= seed_i and j < (seed_i + seeds_range[i_seed]):
        return i
    i += 1


print(part2())
