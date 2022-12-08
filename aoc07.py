file = open("input07.txt", "r")
file.readline()  # root directory, not needed
lines = file.read().split("\n")
file.close()

x = ["/"]
sizes = [0]
locs = [0]

i = 0
while True:
    if lines[i] == "$ cd ..":
        print("CDUP " + lines[i])
        x.pop()
        i += 1
    if lines[i][:4] == "$ cd" and lines[i][5:] != "..":
        print("CDIN " + lines[i])
        x.append(lines[i][5:])
        # exec()
        locs.append([0])
        # break
        i += 1
    if lines[i] == "$ ls":
        print("LIST " + lines[i])
        i += 1
        while lines[i][0] != "$":
            if lines[i][:3] == "dir":
                print("DIRC " + lines[i])
                i += 1
            else:
                print("FILE " + lines[i])
                i += 1
            if lines[i] == "":
                break
    if lines[i] == "":
        break
    # print(i)

    #i += 1
    # if i == 20:
    #     break
print(x)
print(locs)




# dirs = [[]]
# sizes = [[]]
# location = [0]
#
# # exec("location.append(4)")
# # print(location)
#
# for i in range(len(x)):
#     # print(x[i])
#     jdir = 0
#     if x[i] == "$ ls":
#         i += 1
#         while x[i][0] != "$":
#             jdir = 0
#             if x[i][0:3] == "dir":
#                 jdir += 1
#                 print("DIRECTORY", x[i])
#                 i_location = "dirs[" + "][".join([str(l) for l in location]) + "].append("
#                 print("dirs = " + str(dirs))
#                 print(i_location + "\"" + str(x[i].split(" ")[1]) + "\"" + ")")
#                 exec(i_location + "\"" + str(x[i].split(" ")[1]) + "\"" + ")")
#                 i_location = "sizes[" + "][".join([str(l) for l in location]) + "].append([])"
#                 exec(i_location)
#             else:
#                 jdir += 1
#                 print("FILE", x[i])
#                 i_location = "sizes[" + "][".join([str(l) for l in location]) + "].append("
#                 print("sizes = " + str(sizes))
#                 print(i_location + str(x[i].split(" ")[0]) + ")")
#                 exec(i_location + str(x[i].split(" ")[0]) + ")")
#                 # exec(dirs)
#                 # for j in location:
#                 #     break
#             i += 1
#
#         if x[i][0:4] == "$ cd":
#             if x[i] == "$ cd ..":
#                 location.pop()
#             else:
#                 location.append(jdir)
#         i += 1
#         # if i >= 8:
#         #     break
#     # if i >= 12:
#     #     break
#     if x[i][0:4] == "$ cd":
#         if x[i] == "$ cd ..":
#             location.pop()
#         else:
#             location.append(jdir)
#     i += 1
# print("---------------")
# print(dirs)
# print(sizes)
# print(location)