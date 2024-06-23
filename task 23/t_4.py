from functools import lru_cache


@lru_cache(None)
def f(l, r):
    if l < r:
        t = f(l + 1, r)
        if (l // 10) % 10 != 9:
            t += f(l + 10, r)
        return t
    return l == r


print(f(15, 28))  # 5
