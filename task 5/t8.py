
for i in range(1, 10 ** 5):
    a = bin(i)[2:]
    a += str(i % 2) * 2
    r = int(a, 2)

    if r > 115:
        print(i, r)
        break