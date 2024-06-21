m = 10 ** 9

for i in range(1, 1000_000):
    a = bin(i)[2:]
    s = sum([int(i) for i in a])

    a2 = f'{a}{s % 2}'
    s2 = sum([int(i) for i in a2])

    a3 = f'{a2}{s2 % 2}'
    if 80 < int(a3, 2) < m:
        print(i, a, a2, a3, int(a3, 2))
        m = int(a3, 2)
