import re

file = open("input/input19_test.txt", "r")
[workflows, ratings] = [[j for j in i.split("\n")] for i in file.read().split("\n\n")]
file.close()

ratings = [[int(i) for i in re.match("{x=([0-9]+),m=([0-9]+),a=([0-9]+),s=([0-9]+)}", r_i).groups()] for r_i in ratings]
workflows = dict(zip([w_i.split("{")[0] for w_i in workflows], [w_i.split("{")[1].split("}")[0] for w_i in workflows]))
parts_dict = {"x": 0, "m": 1, "a": 2, "s": 3}


def part1():
  sum_accepted = 0
  for rating_i in ratings:
    rule_i = workflows.get("in").split(",")
    i_rule = 0
    while True:
      if rule_i[i_rule] == "A":
        sum_accepted += sum(rating_i)
        break
      elif rule_i[i_rule] == "R":
        break
      if i_rule == len(rule_i) - 1:
        rule_i = workflows.get(rule_i[i_rule]).split(",")
        i_rule = 0
        continue
      test_rating = rating_i[parts_dict.get(rule_i[i_rule][0])]
      if (rule_i[i_rule][1] == ">" and test_rating > int(rule_i[i_rule].split(":")[0][2:])) or \
         (rule_i[i_rule][1] == "<" and test_rating < int(rule_i[i_rule].split(":")[0][2:])):
        if rule_i[i_rule].split(":")[1] == "A":
          sum_accepted += sum(rating_i)
          break
        elif rule_i[i_rule].split(":")[1] == "R":
          break
        else:
          rule_i = workflows.get(rule_i[i_rule].split(":")[1]).split(",")
          i_rule = 0
          continue
      i_rule += 1
  return sum_accepted


for w_i in workflows.values():
  w_i = w_i.split(",")[::-1]
  for w_ii in w_i:
    if w_ii.find("A") == -1:
      continue
    r_ii = w_ii.split(":")[0]
    break
  break
  # break