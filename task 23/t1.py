def f(r, l):
    if r == l:
        return 1
    if r > l:
        return 0
    return f(r + 1, l) + f(r + 3, l) + f(r * 2, l)


print(f(1, 15))  # 448