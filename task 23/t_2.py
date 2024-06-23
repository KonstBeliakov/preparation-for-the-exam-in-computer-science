from functools import lru_cache


@lru_cache(None)
def f(l, r):
    if l == r:
        return 1
    if l > r:
        return 0
    return f(l + 1, r) + f(l + 2, r) + f(l * 3, r)


print(f(2, 8) * f(8, 10) * f(10, 12))  # 60
