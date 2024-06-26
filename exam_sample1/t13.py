mask = [255, 255, 252, 0]
ip = [156, 132, 15, 138]

a = [i & j for i, j in zip(mask, ip)]



print(*[bin(i)[2:].rjust(8, '0') for i in mask])
print(*[bin(i)[2:].rjust(8, '0') for i in ip])
print(*[bin(i)[2:].rjust(8, '0') for i in a])
print(*a)