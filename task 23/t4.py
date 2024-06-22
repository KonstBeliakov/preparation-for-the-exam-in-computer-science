def f(l, r):
    if l == r:
         return 1
    if l > r or l == 6:
         return 0
    return f(l + 2, r) + f(l * 3, r)


print(f(1, 25) * f(25, 63))  # 8