# 27_36882

with open('27_36882_B.txt', 'r', encoding='utf-8') as file:
    n = file.readline()

    l = [[int(i.split()[0]), int(i.split()[1])] for i in file.readlines() if int(i.split()[1]) % 2]

    s_max, s_min = 0, 0
    for i in l:
        s_max += max(i)
        s_min += min(i)

    m1 = None
    for i in l:
        if i[0] % 2 and i[1] % 2:
            if m1 is None or sum(i) < sum(m1):
                m1 = i
    print(f'm1: {m1}, s: {sum(m1)}')

    m2, m3 = None, None
    for i in l:
        if min(i) % 2 and not max(i) % 2:
            if m2 is None or sum(i) < sum(m2):
                m2 = i
        if not min(i) % 2 and max(i) % 2:
            if m3 is None or sum(i) < sum(m3):
                m3 = i
    print(f'm2: {m2}, m3: {m3}')
    print(f'sum: {None if m2 is None or m3 is None else sum(m2) + sum(m3)}')
        
    print(f's_min: {s_min}, s_max: {s_max}')

    max1 = [s_min - min(m1), s_max - max(m1)]
    print(f'max1: {max1}, sum: {sum(max1)}')

    max2 = [s_min - min(m2) - min(m3), s_max - max(m2) - max(m3)]
    print(f'max2: {max2}, sum: {sum(max2)}\n')

    print(f'answer: {max(sum(max1), sum(max2))}')


    
