f = open("input.txt","r")
# x = 0
# max_x = 0
# for i in f:
#     if i in ['\n','\r\n']:
#         if x > max_x:
#             max_x = x
#         x = 0
#     else:
#         x = x + int(i)
# print(max_x)

# x = []
# xi = 0
# for i in f:
#     if i in ['\n','\r\n']:
#         x.append(xi)
#         xi = 0
#     else:
#         xi += int(i)
# x.sort(reverse=True)
# print(sum(x[0:3]))