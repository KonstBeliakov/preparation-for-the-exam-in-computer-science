from functools import lru_cache


@lru_cache(None)
def f(l, r):
    if l < r:
        return f(l + 1, r) + f(l * 2, r)
    return l == r


print(f(1, 12) * f(12, 30))  # 100
