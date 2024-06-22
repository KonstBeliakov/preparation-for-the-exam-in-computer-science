def f(l, r):
    if l == r:
        return 1
    if l < r:
        return 0
    return f(l - 2, r) + f(l - 5, r)


print(f(23, 2))  # 29
