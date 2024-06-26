with open('26.txt', 'r', encoding='utf-8') as file:
    n = int(file.readline())
    l = [[int(line.split()[0]), int(line.split()[1])] for line in file.readlines()]

    l2 = [set() for _ in range(10_001)]

    for i, j in l:
        l2[i].add(j)

    d = {i: s for i, s in enumerate(l2) if s}

    for i in sorted(d, reverse=True):
        t = sorted(d[i])
        for j in range(len(t)):
            if t[j] + 3 in t:
                print(i, t[j] + 1)
                exit()


