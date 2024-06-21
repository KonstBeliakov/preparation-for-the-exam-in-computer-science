m = 10 ** 9

for i in range(1, 10 ** 5):
    a = bin(i)[2:]
    a = a.replace('0', '00')
    a = a.replace('1', '11')

    r = int(a, 2)

    if m > r > 63:
        print(i, r)
        m = r