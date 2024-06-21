
for i in range(1, 10 ** 5):
    a = bin(i)[2:]
    s = sum([int(i) for i in a])
    if s % 2:
        a += '1'
        a = '11' + a[2:]
    else:
        a += '0'
        a = '10' + a[2:]

    r = int(a, 2)
    if r < 35:
        print(i, r)
