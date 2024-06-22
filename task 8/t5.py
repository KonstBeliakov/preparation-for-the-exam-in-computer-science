l = sorted(list('есаул'))

l2 = []
for i1 in l:
    for i2 in l:
        for i3 in l:
            for i4 in l:
                for i5 in l:
                    l2.append(i1 + i2 + i3 + i4 + i5)

n = 0
for i in l2:
    t1 = 'eау'
    for j in t1:
        i.replace(j, '0')

    n += '00' not in i

print(n)