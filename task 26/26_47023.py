# 26_47023

def group_size(line):
    size = 0
    max_size = 0
    index = -1

    line2 = [line[i] if i % 2 else not line[i] for i in range(len(line))]

    for i in range(1, len(line2)):
        if line2[i] == line2[i - 1]:
            size += 1
            if size > max_size:
                max_size = size // 2 + (line[i] % 2)
                index = i
        else:
            size = 1
    return max_size


with open('26_47023.txt', 'r', encoding='utf-8') as file:
    n = int(file.readline())

    l = [[False] * 10_001 for i in range(10_001)]

    for line in file.readlines():
        x, y = map(int, line.split())
        l[x][y] = True

    max_group_size = 0
    index = -1

    for i, line in enumerate(l):
        t = group_size(line)
        if t > max_group_size:
            max_group_size = t
            index = i

    print(f'max_group_size: {max_group_size}')
    print(f'index: {index}')
