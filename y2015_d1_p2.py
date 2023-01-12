# Now, given the same instructions, find the position of the first character that causes him to enter the basement
# (floor -1). The first character in the instructions has position 1, the second character has position 2, and so on.
#
# For example:
#
# ) causes him to enter the basement at character position 1.
# ()()) causes him to enter the basement at character position 5.
# What is the position of the character that causes Santa to first enter the basement?


from input_data import input_data

input_data = input_data(2015, 1)
answer = 0

for position, bracket in enumerate(input_data, start=1):
    if bracket == '(':
        answer += 1
    else:
        answer -= 1
    if answer < 0:
        break

print(position)
