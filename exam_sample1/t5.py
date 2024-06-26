r_min = 10 ** 9

for n in range(1, 10 ** 4):
    a = []
    t = n
    while t > 0:
        a.append(t % 12)
        t //= 12
    a = a[::-1]

    if n % 4:
        a.append(max(a))
    else:
        a = [2] + a + [6, 4]

    r = 0
    for i in a:
        r *= 12
        r += i

    if 1799 < r < r_min:
        print(r)
        r_min = r