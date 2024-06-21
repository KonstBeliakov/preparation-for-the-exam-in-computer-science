import re
for i in range(3123, 10**9, 3123):
    t = re.fullmatch('12\d*63\d5\d', str(i))
    if t is not None:
        print(i)
