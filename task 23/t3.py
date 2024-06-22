def f(l, r):
    if l == r:
        return 1
    if l > r:
        return 0
    return f(l + 1, r) + f(l * 2, r)


print(f(1, 10) * f(10, 20))  # 28