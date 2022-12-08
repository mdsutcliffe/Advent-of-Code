f = open("input3.txt", "r")

lower_case = [chr(i) for i in range(ord("a"), ord("z") + 1)]
upper_case = [chr(i) for i in range(ord("A"), ord("Z") + 1)]
letters = lower_case + upper_case

# score = 0
# for i in f:
#     i0 = i[:len(i) // 2]
#     i1 = i[len(i) // 2:]
#     intersect = list(set(i0) & set(i1))[0]
#     score += letters.index(intersect) + 1
# print(score)

score = 0
while True:
    i0 = f.readline()
    i1 = f.readline()[:-1]
    i2 = f.readline()[:-1]
    print(i0)
    break
    if not i2:
        break
    intersect = list(set(i0) & set(i1) & set(i2))[0]
    score += letters.index(intersect) + 1
print(score)
