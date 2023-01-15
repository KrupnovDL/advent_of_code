# You just finish implementing your winning light pattern when you realize you mistranslated Santa's message from
# Ancient Nordic Elvish.
#
# The light grid you bought actually has individual brightness controls; each light can have a brightness of zero or
# more. The lights all start at zero.
#
# The phrase turn on actually means that you should increase the brightness of those lights by 1.
#
# The phrase turn off actually means that you should decrease the brightness of those lights by 1, to a minimum of zero.
#
# The phrase toggle actually means that you should increase the brightness of those lights by 2.
#
# What is the total brightness of all lights combined after following Santa's instructions?
#
# For example:
#
# turn on 0,0 through 0,0 would increase the total brightness by 1.
# toggle 0,0 through 999,999 would increase the total brightness by 2000000.


from input_data import input_data
import numpy as np


input_data = input_data(2015, 6).splitlines()
grid = np.zeros([1000, 1000])

for line in input_data:
    line = line.replace(",", " ").split()
    x1 = int(line[-5])
    x2 = int(line[-2]) + 1
    y1 = int(line[-4])
    y2 = int(line[-1]) + 1
    if line[1] == "on":
        grid[x1:x2, y1:y2] += 1
    elif line[1] == "off":
        grid[x1:x2, y1:y2] -= 1
    else:
        grid[x1:x2, y1:y2] += 2
    grid[x1:x2, y1:y2][grid[x1:x2, y1:y2] < 0] = 0

print(int(np.sum(grid)))
