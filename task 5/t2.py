
for i in range(100, 1000):
    a, b, c = list(str(i))
    a, b, c = int(a) ** 2, int(b) ** 2, int(c) ** 2

    n1 = a + b
    n2 = b + c
    n1, n2 = min(n1, n2), max(n1, n2)

    n = int(f'{n2}{n1}')

    if n == 9010:
        print(i)
    