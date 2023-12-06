file = "./input/input05.txt"

num_nice_words = 0
with open("./input/input05.txt", "r") as f:
    for word in f:
        num_vowels = 0
        double_letter = False
        bad_pair = False
        for index, letter in enumerate(word):
            if letter in "aeiou":
                num_vowels += 1
            if index > 0 and letter == word[index - 1]:
                double_letter = True
            if index > 0 and word[index - 1:index + 1] in ["ab", "cd", "pq", "xy"]:
                bad_pair = True
        if num_vowels < 3:
            # print(word + " = too few vowels")
            continue
        if not double_letter:
            # print(word + " = no double letter")
            continue
        if bad_pair:
            # print(word + " = bad pair")
            continue
        # print(word + " = nice word!")
        num_nice_words += 1
print(num_nice_words)

num_nice_words = 0
# with open(file,"r") as f:
#     for word in f:
#         for letter in range(2)

x = "abcdefabcdefefjdhahgdlkajflabxabjfdljalfd"

# for ind in range(0,len(x)-2):
#     print(x[ind:ind+3])
#     if x[ind] == x[ind+2]:
#         print("sandwich!")
#     if x[ind] == x[ind+1]

num_nice_words = 0
with open("./input/input05.txt", "r") as f:
    for x in f:
        # x = "ieodomkazucvgmuy"
        good_pair = False
        good_repeat = False
        print(x)
        for index in range(len(x)-3):
            print(x[index:index+2])
            for index2 in range(index+2,len(x)+1):
                print(x[index2:index2+2])
                if x[index:index+2] == x[index2:index2+2]:
                    good_pair = True
                    break
            if x[index] == x[index+2]:
                good_repeat = True
        if x[-3] == x[-1]:
            good_repeat = True
            # if x[index:index+2] == x[index+2:index+4]:
            #     good_
        # break
#
#         for index, letter in enumerate(x):
#             if (len(x) - index) < 3:
#                 break
#             pair = x[index:index+2]
#             for index2 in range(index+1, len(x)+1):
#                 pair2 = x[index2:index2+2]
#                 if pair == pair2:
#                     good_pair = True
#                     print("    good pair: " + pair + " = " + pair2)
#             if letter == x[index+2]:
#                 good_repeat = True
#                 print("    good repe: " + letter + " = " + x[index+2])
#
        if good_pair and good_repeat:
            num_nice_words += 1
            print("good word    " + x)
        else:
            print("bad word     " + x)
#
print(num_nice_words)