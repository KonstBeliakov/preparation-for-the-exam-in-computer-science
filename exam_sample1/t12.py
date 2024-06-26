for n in range(1, 10 ** 4):
    s = '3' + '9' * n + '5' * n

    while '39' in s or '35' in s or '555' in s:
        if '39' in s:
            s = s.replace('39', '55', 1)
        if '35' in s:
            s = s.replace('35', '9', 1)
        if '555' in s:
            s = s.replace('555', '3')

    s2 = sum([int(i) for i in s])
    if s2 % len(s) == n:
        print(n)
