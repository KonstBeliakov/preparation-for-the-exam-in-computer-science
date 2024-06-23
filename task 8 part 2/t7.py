n = 0

for i in range(16 ** 2, 16 ** 3):
    a = hex(i)[2:]
    n += len(set(a)) == len(a) and all([int(a[j], 16) % 2 != int(a[j + 1], 16) % 2 for j in range(len(a) - 1)])

print(n)  # 840
