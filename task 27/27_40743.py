# 27_40743

# решение будет работать только для пункта А (для В нужно писать дерево отрезков)

k = 30

with open('27_40743_A.txt', 'r', encoding='utf-8') as file:
    n = int(file.readline())

    l = [int(i) for i in file.readlines()]

    max_s = 0
    for i in range(len(l)):
        s = 0
        even = 0
        for j in range(i, len(l)):
            s += l[j]
            if l[j] > 0 and l[j] % 2 == 0:
                even += 1
            if even % k == 0:
                max_s = max(max_s, s)

    print(f'max_s: {max_s}')
