# 25_27850

def prime(x):
    if x == 1:
        return False
    for i in range(2, x):
        if i * i > x:
            return True
        if x % i == 0:
            return False

l = 245_690
r = 245_756

for i in range(l, r):
    if prime(i):
        print(i - l + 1, i)
