# 26_33198
with open('26_33198.txt', 'r', encoding='utf-8') as file:
    n, m = map(int, file.readline().split())

    l = sorted([int(i) for i in file.readlines()])

    weight = 0
    max_n = 0

    used = [False] * len(l)

    for i in l:
        if 200 <= i <= 210:
            weight += i
            max_n += 1
            used[i] = True

    for i in range(len(l)):
        if not used[i]:
            if weight + l[i] > m:
                break
            weight += l[i]
            max_n += 1
        
    print(f'max_n: {max_n}')
    print(f'weight: {weight}/{m}\n')

    for j in range(max_n):
        for i in range(len(l) - 1, -1, -1):
            if weight + l[i] - l[j] <= m and not used[i]:
                used[j] = False
                used[i] = True
                weight = weight + l[i] - l[j]
                print(f'remove l[{j}]: {l[j]}, add l[{i}]: {l[i]}')
                break

        print(f'weight: {weight}/{m}\n')

        if weight == m:
            print('full')
            break
