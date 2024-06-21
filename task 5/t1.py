
for i in range(100, 1000):
    n1 = int(str(i)[0]) * int(str(i)[1])
    n2 = int(str(i)[1]) * int(str(i)[2])

    n1, n2 = min(n1, n2), max(n1, n2)

    n = int(f'{n2}{n1}')

    if n == 240:
        print(i)