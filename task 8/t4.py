'''n = 0

for i in range(1, 16 ** 5):
    x = hex(i)[2:]
    if len(x) in [3, 5] and all([x[i] > x[i + 1] for i in range(len(x) - 1)]):
        n += 1

print(n)  # 4928
'''
n = 0

for i1 in range(1, 16):
    for i2 in range(0, i1):
        for i3 in range(0, i2):
            n += 1

for i1 in range(1, 16):
    for i2 in range(0, i1):
        for i3 in range(0, i2):
            for i4 in range(0, i3):
                for i5 in range(0, i4):
                    n += 1
print(n)  # 4928