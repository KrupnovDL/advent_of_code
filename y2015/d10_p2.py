# Neat, right? You might also enjoy hearing John Conway talking about this sequence (that's Conway of Conway's Game of
# Life fame).
#
# Now, starting again with the digits in your puzzle input, apply this process 50 times. What is the length of the new
# result?


def look_and_say(string):
    digit = string[0]
    number_of_digits = 1
    result = ''
    for current_digit in string[1:]:
        if current_digit == digit:
            number_of_digits += 1
        else:
            result += str(number_of_digits) + digit
            digit = current_digit
            number_of_digits = 1
    else:
        result += str(number_of_digits) + digit
    return result


input_data = "1113122113"

for i in range(50):
    input_data = look_and_say(input_data)

print(len(input_data))
