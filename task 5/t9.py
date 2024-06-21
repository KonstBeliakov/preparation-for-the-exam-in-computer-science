
for i in range(2, 10 ** 5):
    a = bin(i)[2:-1]
    if i % 2:
        a += '10'
    else:
        a += '01'
    r = int(a, 2)
    if r == 2018:
        print(i)
