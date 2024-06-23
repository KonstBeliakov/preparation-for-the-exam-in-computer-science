a = 0

for i in range(16 ** 2, 16 ** 3):
    n = hex(i)[2:]
    if all([int(n[i], 16) >= int(n[i + 1], 16) for i in range(len(n) - 1)]):
        a += 1

print(a)  # 815
