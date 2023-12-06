file = open("input01.txt", "r")
x = file.read().split("\n")
file.close()

digits = [str(i) for i in range(10)]

# PART 1
sum_calibration = 0
for i in x:
    digit_first = 0
    for j in i:
        if j in digits:
            digit_first = j
            break
    digit_last = 0
    for j in i[::-1]:
        if j in digits:
            digit_last = j
            break
    calibration_value = int(digit_first + digit_last)
    sum_calibration += calibration_value
print(sum_calibration)

# PART 2
digits_string = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"] + [str(i) for i in range(10)]
digits_string_rev = [i[::-1] for i in digits_string]

dict_digits = dict(zip(digits_string, [i+1 for i in range(9)] + [str(i) for i in range(10)]))
dict_digits_rev = dict(zip(digits_string_rev, [i+1 for i in range(9)] + [str(i) for i in range(10)]))

sum_calibration = 0
for i in x:
    first_instance = [i.find(j) for j in digits_string]
    digit_first = list(dict_digits.values())[first_instance.index(min(filter(lambda a: a >= 0, first_instance)))]

    i_rev = i[::-1]
    last_instance = [i_rev.find(j) for j in digits_string_rev]
    digit_last = list(dict_digits_rev.values())[last_instance.index(min(filter(lambda a: a >= 0, last_instance)))]
    calibration_value = int(str(digit_first) + str(digit_last))
    sum_calibration += calibration_value
print(sum_calibration)