def m(x):
    for i in range(2, x):
        if i ** 2 > x:
            return 0
        if x % i == 0:
            return i + x // i


for i in range(700_001, 10 ** 6):
    if m(i) % 10 == 8:
        print(i, m(i))