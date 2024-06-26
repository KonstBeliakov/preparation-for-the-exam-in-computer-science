print(4 ** 11)

for x in range(1, 12):
    a = int('90ab', 13) + x * 13 ** 2
    b = int('46c', 16) + x * 16 ** 3
    c = int('b70', 15) + x

    if (a + b - c) % 14 == 0:
        t = (a + b - c) // 14
        print(x, t)