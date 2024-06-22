
l = sorted(list('мария'))

l2 = []

for i1 in l:
    for i2 in l:
        for i3 in l:
            for i4 in l:
                l2.append(i1 + i2 + i3 + i4)

print(l2[210])  # 'ирма'
