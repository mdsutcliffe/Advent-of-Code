import itertools
import re
import math

file = open("input/input12_test.txt", "r")
x = file.read().split("\n")
file.close()

criteria = x[0].split()[1].split(",")
record = x[0].split()[0]


def check_arrangement(record, criteria):
  pattern = "[#]{" + "}[.]+[#]{".join([str(i) for i in criteria]) + "}"
  pattern = "".join(pattern)
  m = re.search(pattern, record)
  return m is not None

total = 0
for i_x, x_i in enumerate(x):
  print(str(i_x) + " of " + str(len(x)))
  criteria = [int(i) for i in x_i.split()[1].split(",")]
  record = x_i.split()[0]

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
      total += 1

print(total)

# part 2

total = 0
for i_x, x_i in enumerate(x):
  print(str(i_x) + " of " + str(len(x)))
  criteria = [int(i) for i in x_i.split()[1].split(",")]*5
  if list(x_i.split()[0])[-1] == ".":
    record = "?".join([x_i.split()[0]] * 5)
  else:
    record = ".".join([x_i.split()[0]] * 5)

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
      total += 1
  print(total)

print(total)
