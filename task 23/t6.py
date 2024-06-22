def f(l, r):
    if l == r:
        return 1
    if l > r or l == 43:
        return 0
    return f(l + 2, r) + f(l * 2 - 1, r) + f(l * 2 + 1, r)


print(f(7, 63))  # 116
