
for i in range(1, 10 ** 4):
    a = bin(i)[2:]
    s = a.count('1')

    if s % 2 == 0:
        a += '0'
        a = '10' + a[2:]
    else:
        a += '1'
        a = '11' + a[2:]

    r = int(a, 2)

    if r < 35:
        print(i)