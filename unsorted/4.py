
def f(x):
    s = set()
    t = 0
    for i in range(2, x):
        if x % i == 0:
            s.add(i)
            s.add(x // i)
        if i * i > x:
            break
    return None if (len(s) < 5) else sorted(s)[:-6:-1]


n = 300_000_001

for i in range(n, 10**9):
    t = f(i)
    if t is not None:
        print(i, t)
