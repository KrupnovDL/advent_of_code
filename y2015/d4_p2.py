# Now find one that starts with six zeroes.


import hashlib


input_data = "yzbqklnj"

i = 1000000
while hashlib.md5((input_data + str(i)).encode()).hexdigest()[:6] != "000000":
    i += 1

print(i)
