n = 0

for i in range(10 ** 6, 10 ** 7, 5):
    a = str(i)
    if len(set(a)) == len(a) and all([int(a[j]) % 2 != int(a[j + 1]) % 2 for j in range(len(a) - 1)]):
        n += 1

print(n)  # 2880
