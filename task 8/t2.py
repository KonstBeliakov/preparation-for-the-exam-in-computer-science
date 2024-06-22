l = sorted(list('лемур'))

n = 0

for i1 in l:
    for i2 in l:
        for i3 in l:
            for i4 in l:
                n += 1
                if i1 == 'л':
                    print(n) # 126
                    exit()
