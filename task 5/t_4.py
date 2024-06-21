min_r = 10 ** 9

def to_6(x):
    a = ''
    while x > 0:
        a += str(x % 6)
        x //= 6
    return a[::-1]


for n in range(1, 10 ** 5):
    a = to_6(n)

    if n % 3 == 0:
        a += a[:2]
    else:
        a += to_6((n % 3) * 10)

    r = int(a, 6)
    if 680 < r < min_r:
        min_r = r
        print(f'n: {n}, r: {r}')