import hashlib

x = "iwrupvqb"

i = 1
while True:
    xi = x + str(i)
    yi = hashlib.md5(xi.encode('utf-8')).hexdigest()
    if yi[0:5] == "00000":
        print(xi)
        break
    i += 1

print("Lowest #: " + str(i))

# part 2
i = 1
while True:
    xi = x + str(i)
    yi = hashlib.md5(xi.encode('utf-8')).hexdigest()
    if yi[0:6] == "000000":
        print(xi)
        break
    i += 1

print("Lowest #: " + str(i))