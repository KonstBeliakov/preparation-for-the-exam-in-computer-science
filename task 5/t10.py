
for i in range(80, 10 ** 4):
    a = bin(i)[2:]

    for _ in range(3):
        ones = a.count('1')
        zeros = a.count('0')

        if ones == zeros:
            a += a[-1]
        elif ones < zeros:
            a += '1'
        else:
            a += '0'

    r = int(a, 2)

    if r % 2 == 0 and r % 4:
        print(r)
        break