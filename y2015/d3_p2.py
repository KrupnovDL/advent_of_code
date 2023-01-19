# The next year, to speed up the process, Santa creates a robot version of himself, Robo-Santa, to deliver presents
# with him.
#
# Santa and Robo-Santa start at the same location (delivering two presents to the same starting house), then take turns
# moving based on instructions from the elf, who is eggnoggedly reading from the same script as the previous year.
#
# This year, how many houses receive at least one present?
#
# For example:
#
# ^v delivers presents to 3 houses, because Santa goes north, and then Robo-Santa goes south.
# ^>v< now delivers presents to 3 houses, and Santa and Robo-Santa end up back where they started.
# ^v^v^v^v^v now delivers presents to 11 houses, with Santa going one direction and Robo-Santa going the other.


from input_data import input_data


input_data = input_data(2015, 3)
santa_location = [0, 0]
robo_santa_location = [0, 0]
houses = {(0, 0): 2}
santa_turn = True

for element in input_data:
    if santa_turn:
        location = santa_location
        santa_turn = False
    else:
        location = robo_santa_location
        santa_turn = True
    if element == '>':
        location[0] += 1
    elif element == '<':
        location[0] -= 1
    elif element == '^':
        location[1] += 1
    elif element == 'v':
        location[1] -= 1
    if tuple(location) in houses:
        houses[tuple(location)] += 1
    else:
        houses[tuple(location)] = 1

print(len(houses))
