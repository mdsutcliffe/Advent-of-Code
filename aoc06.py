file = open("input06.txt", "r")
x = file.readline()[:-1]
file.close()

packet_size = 4

for i in range(len(x)-packet_size-1):
    if len(set(x[i:(i+packet_size)])) == packet_size:
        print(i + packet_size)
        break

packet_size = 14

for i in range(len(x)-packet_size-1):
    if len(set(x[i:(i+packet_size)])) == packet_size:
        print(i + packet_size)
        break
