def f(l, r):
    if l == r:
         return 1
    if l > r:
         return 0
    return f(l + 1, r) + f(2 * l, r) + f(2 * l + 1, r) + f(l * 10, r)


print(f(1, 15))  # 84