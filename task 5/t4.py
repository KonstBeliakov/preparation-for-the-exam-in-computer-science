m = 10 ** 9

for i in range(1, 10 ** 6):
    a = bin(i)[2:]
    a2 = a + a[-1]

    s = sum([int(i) for i in a2])
    a3 = f'{a2}{s % 2}'

    s = sum([int(i) for i in a3])
    a4 = f'{a3}{s % 2}'

    r = int(a4, 2)

    if m > r > 144:
        print(r)
        m = r