import re

file = open("input03.txt", "r")
x = file.read().split("\n")
file.close()


def part1():
  line_length = len(x[0])
  n_rows = len(x)
  part_numbers = []
  for i, x_i in enumerate(x):
    nums = re.findall(pattern="[0-9]+", string=x_i)
    nums_index = [j.start() for j in re.finditer(pattern="[0-9]+", string=x_i)]
    for ii, num_i in enumerate(nums):
      start_i = nums_index[ii]
      xx = [ii[max([0, start_i - 1]):(start_i + len(num_i) + 1)] for ii in
            x[max(0, i - 1):(min(n_rows - 1, i + 1) + 1)]]
      xx = "".join(xx)
      xx = re.sub("[.0-9]", "", xx)
      if len(xx) > 0:
        part_numbers.append(int(num_i))
  return sum(part_numbers)


print(part1())


def part2():
  gear_ratios = []
  for i, x_i in enumerate(x):
    nums = re.findall(pattern="[0-9]+", string=x_i)
    nums_index = [j.start() for j in re.finditer(pattern="[0-9]+", string=x_i)]
    gears_index = [gi.start() for gi in re.finditer(pattern="\*", string=x_i)]
    for j in gears_index:
      gear_nums = []
      nums_before = re.findall(pattern="[0-9]+", string=x[i - 1])
      nums_before_index = [k.start() for k in re.finditer(pattern="[0-9]+", string=x[i - 1])]
      for ki, k in enumerate(nums_before):
        num_range = [nums_before_index[ki] + a for a in range(len(k))]
        if any([(b >= (j - 1) and b <= (j + 1)) for b in num_range]):
          gear_nums.append(int(k))

      for ki, k in enumerate(nums):
        num_range = [nums_index[ki] + a for a in range(len(k))]
        if any([(b >= (j - 1) and b <= (j + 1)) for b in num_range]):
          gear_nums.append(int(k))

      nums_after = re.findall(pattern="[0-9]+", string=x[i + 1])
      nums_after_index = [k.start() for k in re.finditer(pattern="[0-9]+", string=x[i + 1])]
      for ki, k in enumerate(nums_after):
        num_range = [nums_after_index[ki] + a for a in range(len(k))]
        if any([(b >= (j - 1) and b <= (j + 1)) for b in num_range]):
          gear_nums.append(int(k))

      if len(gear_nums) == 2:
        gear_ratios.append(gear_nums[0] * gear_nums[1])
  return sum(gear_ratios)


print(part2())
