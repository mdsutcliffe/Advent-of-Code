import itertools
import re
import math

file = open("input/input12_test.txt", "r")
x = file.read().split("\n")
file.close()


def check_arrangement(record, criteria):
  pattern = "[#]{" + "}[.]+[#]{".join([str(i) for i in criteria]) + "}"
  pattern = "".join(pattern)
  m = re.search(pattern, record)
  return m is not None

def part1():
  total = []
  for i_x, x_i in enumerate(x):
    criteria = [int(i) for i in x_i.split()[1].split(",")]
    record = x_i.split()[0]
    total_i = 0

    dof = record.count("?")
    q_inds = [ij for ij, j in enumerate(record) if j == "?"]
    missing_damaged = sum(criteria) - record.count("#")
    missing_working = dof - missing_damaged

    p = ["."]*missing_working + ["#"]*missing_damaged
    all_records = []

    for pi in itertools.combinations(q_inds, missing_damaged):
      ri = list(record)
      for qi in pi:
        ri[qi] = "#"
      ri = "".join(ri).replace("?", ".")
      if check_arrangement(ri, criteria):
        total_i += 1
    total.append(total_i)
  return total, sum(total)


print(part1()[1])

# part 1 redo
def check_arrangement(record, criteria):
  pattern = "[#]{" + "}[.]+[#]{".join([str(i) for i in criteria]) + "}"
  pattern = "".join(pattern)
  m = re.search(pattern, record)
  return m is not None
# def recursive_check(record, criteria):
#   missing_working = sum(criteria) - record.count("#")
#   missing_damaged = record.count("?") - missing_working
#   if missing_damaged == 1 or missing_working == 1:
#     return 1
#   if record[0] == "?"

total = []
for x_i in x:
  criteria = [int(i) for i in x_i.split()[1].split(",")]
  record = x_i.split()[0]
  total_i = 0

  dof = record.count("?")
  q_inds = [ij for ij, j in enumerate(record) if j == "?"]
  missing_damaged = sum(criteria) - record.count("#")
  missing_working = dof - missing_damaged

  p = ["."]*missing_working + ["#"]*missing_damaged
  all_records = []

  for pi in itertools.combinations(q_inds, missing_damaged):
    ri = list(record)
    for qi in pi:
      ri[qi] = "#"
    ri = "".join(ri).replace("?", ".")
    if check_arrangement(ri, criteria):
      total_i += 1
  total.append(total_i)
  break










# total_part1 = part1()[0]



#
# # part 2
# #
# total = []
# for i_x, x_i in enumerate(x):
#   print(str(i_x) + " of " + str(len(x)))
#   criteria = [int(i) for i in x_i.split()[1].split(",")]*5
#   if list(x_i.split()[0])[-1] != "?":
#     record = "?".join([x_i.split()[0]] * 5)
#   else:
#     record = ".".join([x_i.split()[0]] * 5)
#     total.append(total_part1[i_x] ** 5)
#     continue
#   total_i = 0
#
#   dof = record.count("?")
#   q_inds = [ij for ij, j in enumerate(record) if j == "?"]
#   missing_damaged = sum(criteria) - record.count("#")
#   missing_working = dof - missing_damaged
#
#   p = ["."]*missing_working + ["#"]*missing_damaged
#   all_records = []
#
#   for pi in itertools.combinations(q_inds, missing_damaged):
#     ri = list(record)
#     for qi in pi:
#       ri[qi] = "#"
#     ri = "".join(ri).replace("?", ".")
#     if check_arrangement(ri, criteria):
#       total_i += 1
#   total.append(total_i)
# print(total)
# #
# # def part1():
# #   total = []
# #   for i_x, x_i in enumerate(x):
# #     criteria = [int(i) for i in x_i.split()[1].split(",")]
# #     record = x_i.split()[0]
# #     total_i = 0
# #
# #     dof = record.count("?")
# #     q_inds = [ij for ij, j in enumerate(record) if j == "?"]
# #     missing_damaged = sum(criteria) - record.count("#")
# #     missing_working = dof - missing_damaged
# #
# #     p = ["."]*missing_working + ["#"]*missing_damaged
# #     all_records = []
# #
# #     for pi in itertools.combinations(q_inds, missing_damaged):
# #       ri = list(record)
# #       for qi in pi:
# #         ri[qi] = "#"
# #       ri = "".join(ri).replace("?", ".")
# #       if check_arrangement(ri, criteria):
# #         total_i += 1
# #     total.append(total_i)
# #   return total, sum(total)
# #
# #
# # print(total)
