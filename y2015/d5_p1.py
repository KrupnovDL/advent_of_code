# --- Day 5: Doesn't He Have Intern-Elves For This? ---
# Santa needs help figuring out which strings in his text file are naughty or nice.
#
# A nice string is one with all of the following properties:
#
# It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
# It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
# It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
# For example:
#
# ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a double letter (...dd...), and none of
# the disallowed substrings.
# aaa is nice because it has at least three vowels and a double letter, even though the letters used by different rules
# overlap.
# jchzalrnumimnmhp is naughty because it has no double letter.
# haegwjzuvuyypxyu is naughty because it contains the string xy.
# dvszwmarrgswjxmb is naughty because it contains only one vowel.
# How many strings are nice?


from input_data import input_data
import re


input_data = input_data(2015, 5).split()
nice_strings = []

for string in input_data:
    if any(x in string for x in ("ab", "cd", "pq", "xy")):
        continue
    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            break
    else:
        continue
    if len(re.findall(r"[aeiou]", string)) < 3:
        continue
    nice_strings.append(string)

print(len(nice_strings))
