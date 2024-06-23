from functools import lru_cache


@lru_cache(None)
def f(l, r):
    if l < r:
        return f(l + 1, r) + f(l + 2, r) + f(l * 2 + 1, r)
    return l == r


print(f(2, 10))  # 47
