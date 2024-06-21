def f(x):
    for i in range(2, x):
        if i * i > x:
            return 0
        if x % i == 0:
            return i + x // i
    return 0

n = 452_022

t = 0

for i in range(n, 10 ** 6):
    if f(i) % 7 == 3:
        print(i, f(i))
        t += 1
    if t == 5:
        break
