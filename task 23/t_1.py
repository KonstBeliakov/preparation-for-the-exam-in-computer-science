from functools import lru_cache


@lru_cache(None)
def f(l, r):
    if l == r:
        return 1
    if l > r:
        return 0
    return f(l + 1, r) + f(l * 2, r) + f(l ** 2, r)


print(f(5, 154))  # 8966
