n = 0

for i in range(16 ** 3, 16 ** 4):
    a = hex(i)[2:]
    n += a.count('9') == 1 and all([int(a[j], 16) % 2 != int(a[j + 1], 16) % 2 for j in range(len(a) - 1)])

print(n)  # 1680
