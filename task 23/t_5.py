from functools import lru_cache


@lru_cache(None)
def f(l, r):
    if l < r:
        return f(l + 1, r) + f(l * 10 + 3, r)
    return l == r


print(f(3, 462))  # 60
