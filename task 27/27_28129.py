# 27_28129

with open('28129_B.txt', 'r', encoding='utf-8') as file:
    n = int(file.readline())

    l = [int(i) for i in file.readlines()]

    d = 160
    p = 7

    pair = [0, 0]
    
    for i in l:
        for j in l:
            if i % d != j % d and (i % 7 == 0 or j % 7 == 0):
                if i + j > sum(pair):
                    pair = [i, j]
    print(*pair)
