for n in range(1, 10 ** 5):
    a = ''
    t = n
    while t > 0:
        a += str(t % 7)
        t //= 7
    a = a[::-1]

    if a.count('2') % 2 == 0:
        a += '555'
    else:
        a = '1' + a

    r = int(a, 7)
    if r < 3799:
        print(f'n: {n}, r: {r}')
