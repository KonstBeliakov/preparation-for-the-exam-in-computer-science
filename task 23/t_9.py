from functools import lru_cache


@lru_cache(None)
def f(l, r):
    if l > r:
        return f(l - 8, r) + f(l // 2, r)
    return l == r


print(f(102, 43) * f(43, 5))  # 8
