import math
import re

file = open("input02.txt", "r")
x = file.read().split("\n")
file.close()

def part1(x):
  rgb_cubes = [12, 13, 14]
  game_sum = 0
  for xi in x:
    game_id = int(xi[5:xi.find(":")])
    n_red = [int(red_i[0:-4]) for red_i in re.findall(pattern="[0-9]+ red", string=xi)]
    n_green = [int(green_i[0:-6]) for green_i in re.findall(pattern="[0-9]+ green", string=xi)]
    n_blue = [int(blue_i[0:-5]) for blue_i in re.findall(pattern="[0-9]+ blue", string=xi)]
    rgb_possible = [max(rgb_i) <= rgb for rgb_i, rgb in zip([n_red, n_green, n_blue], rgb_cubes)]
    if all(rgb_possible):
      game_sum += game_id
  return game_sum

print(part1(x))

def part2(x):
  power_sum = 0
  for xi in x:
    max_red = max([int(red_i[0:-4]) for red_i in re.findall(pattern="[0-9]+ red", string=xi)])
    max_green = max([int(green_i[0:-6]) for green_i in re.findall(pattern="[0-9]+ green", string=xi)])
    max_blue = max([int(blue_i[0:-5]) for blue_i in re.findall(pattern="[0-9]+ blue", string=xi)])
    power = math.prod([max_red, max_green, max_blue])
    power_sum += power
  return power_sum

print(part2(x))