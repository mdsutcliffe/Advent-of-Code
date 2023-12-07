# input_file = "input/input07_test.txt"
input_file = "input/input07.txt"
with open(input_file, "r") as f:
  x = f.read().split("\n")

hands = [i.split()[0] for i in x]
bids = [int(i.split()[1]) for i in x]


def group_rank(table):
  group = 6
  if max(table) == 5:
    group = 0
  elif max(table) == 4:
    group = 1
  elif 3 in set(table) and 2 in set(table):
    group = 2
  elif max(table) == 3:
    group = 3
  elif table.count(2) == 2:
    group = 4
  elif max(table) == 2:
    group = 5
  return group


def sort_hands(hands, bids, cards):
  for rank_group in range(len(hands)):
    if len(hands[rank_group]) <= 1:
      continue
    for i in range(len(hands[rank_group])):
      for j in range(i + 1, len(hands[rank_group])):
        flag = False
        for k in range(5):
          if hands[rank_group][i][k] != hands[rank_group][j][k]:
            if cards.get(hands[rank_group][i][k]) > cards.get(hands[rank_group][j][k]):
              # SWAP
              hands[rank_group][i], hands[rank_group][j] = \
                hands[rank_group][j], hands[rank_group][i]
              bids[rank_group][i], bids[rank_group][j] = \
                bids[rank_group][j], bids[rank_group][i]
              break
            flag = True
          if flag:
            break
  return hands, bids


def part1():
  cards = ["A", "K", "Q", "J", "T"] + [str(i) for i in range(9, 1, -1)]
  cards = dict(zip(cards, list(range(len(cards)))))

  hands_ranked = [[] for i in range(7)]
  bids_ranked = [[] for i in range(7)]
  for i_hand in range(len(hands)):
    table_i = [hands[i_hand].count(j) for j in cards]
    rank_group = group_rank(table_i)
    hands_ranked[rank_group].append(hands[i_hand])
    bids_ranked[rank_group].append(bids[i_hand])

  bids_ranked = sort_hands(hands_ranked, bids_ranked, cards)[1]

  bids_flat = [i for j in bids_ranked for i in j]
  ranks_flat = list(range(len(hands), 0, -1))

  scores = [bids_flat[i]*ranks_flat[i] for i in range(len(hands))]
  return sum(scores)


print(part1())


def part2():
  cards = ["A", "K", "Q", "T"] + [str(i) for i in range(9, 1, -1)]
  cards = dict(zip(cards, list(range(len(cards)))))

  hands_for_ranking = hands.copy()
  hands_ranked = [[] for i in range(7)]
  bids_ranked = [[] for i in range(7)]
  for i_hand in range(len(hands_for_ranking)):
    table_i = [hands_for_ranking[i_hand].count(j) for j in cards]
    hands_for_ranking[i_hand] = hands_for_ranking[i_hand].replace("J",
                                                                  list(cards.keys())[(table_i.index(max(table_i)))])
    table_i = [hands_for_ranking[i_hand].count(j) for j in cards]
    rank_group = group_rank(table_i)
    hands_ranked[rank_group].append(hands[i_hand])
    bids_ranked[rank_group].append(bids[i_hand])

  cards = ["A", "K", "Q", "T"] + [str(i) for i in range(9, 1, -1)] + ["J"]
  cards = dict(zip(cards, list(range(len(cards)))))

  bids_ranked = sort_hands(hands_ranked, bids_ranked, cards)[1]

  bids_flat = [i for j in bids_ranked for i in j]
  ranks_flat = list(range(len(hands), 0, -1))

  scores = [bids_flat[i] * ranks_flat[i] for i in range(len(hands))]
  return sum(scores)


print(part2())
