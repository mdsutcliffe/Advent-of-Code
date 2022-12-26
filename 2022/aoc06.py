file = open("input/input06.txt", "r")
x = file.readline()[:-1]
file.close()


def find_marker(buffer, packet_size):
    for i in range(len(buffer) - packet_size - 1):
        if len(set(buffer[i:(i + packet_size)])) == packet_size:
            return (i + packet_size)


part1 = find_marker(x, 4)
part2 = find_marker(x, 14)

print("Part 1: " + str(part1))
print("Part 2: " + str(part2))
