for n in range(1, 10 ** 4):
    a = ''
    t = n
    while t > 0:
        a += str(t % 4)
        t //= 4
    a = a[::-1]

    if len(a) % 2 == 0:
        a = a[:len(a) // 2] + '0' + a[len(a) // 2:]

    r = int(a)

    if r <= 180:
        print(n, r)