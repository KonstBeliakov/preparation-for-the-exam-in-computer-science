def to_3(x):
    a = ''
    while x > 0:
        a += str(x % 3)
        x //= 3
    return a[::-1]


for n in range(1, 10 ** 4):
    a = to_3(n)

    if n % 2 == 0:
        a = '1' + a + '00'
    else:
        s = sum([int(i) for i in a])
        s3 = to_3(s)
        a = a + s3

    r = int(a, 3)
    if r > 168:
        print(f'n: {n}, r: {r}')
        break
