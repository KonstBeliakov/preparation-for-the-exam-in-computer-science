l = sorted(list('привычка'))

l2 = []
n = 0

for i1 in l:
    for i2 in l:
        for i3 in l:
            for i4 in l:
                for i5 in l:
                    n += 1
                    if n % 5:
                        l2.append(i1 + i2 + i3 + i4 + i5)

for i, word in enumerate(l2):
    if len(set(word)) == len(word) and all([i in 'првчк' for i in word]):
        print(i + 1)  # 4754
        break
