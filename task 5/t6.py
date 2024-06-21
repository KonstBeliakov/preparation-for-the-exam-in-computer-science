
d = {}
for i in range(1, 10 ** 5):
    a = bin(i)[2:]
    s = sum([int(i) for i in a])
    a += str(s % 2)

    s = sum([int(i) for i in a])
    a += str(s % 2)

    b = int(a, 2)
    if b < 80:
        d[b] = d.get(b, 0) + 1

print(len(d), d)