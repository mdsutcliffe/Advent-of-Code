file = open("./2024/input01.txt", "r")
x = file.read().split("\n")
file.close()

# part 1
x_left = [int(i.split()[0]) for i in x]
x_right = [int(i.split()[1]) for i in x]

x_left.sort()
x_right.sort()

part1 = sum([abs(i - j) for i, j in zip(x_left, x_right)])
print(part1)

# part 2
part2 = sum([i * x_right.count(i) for i in x_left])
print(part2)
