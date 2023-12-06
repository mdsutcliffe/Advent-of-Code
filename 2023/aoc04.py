file = open("input04.txt", "r")
x = file.read().split("\n")
file.close()


def part1():
  total_points = 0
  for x_i in x:
    winning_nums = [int(i) for i in x_i.split(": ")[1].split(" |")[0].split()]
    my_nums = [int(i) for i in x_i.split("| ")[1].split()]
    winners = len(set(my_nums).intersection(set(winning_nums)))
    if winners > 0:
      total_points += 2**(winners - 1)
  return total_points


print(part1())


def part2():
  n_cards = [1]*len(x)
  for i, x_i in enumerate(x):
    winning_nums = [int(i) for i in x_i.split(": ")[1].split(" |")[0].split()]
    my_nums = [int(i) for i in x_i.split("| ")[1].split()]
    winners = len(set(my_nums).intersection(set(winning_nums)))
    if winners > 0:
      n_cards[(i+1):(i+1+winners)] = [j + n_cards[i] for j in n_cards[(i+1):(i+1+winners)]]
  return sum(n_cards)


print(part2())
