def f(x):
    a, b = 0, 0
    while x % 2 == 0:
        a += 1
        x //= 2
    while x % 5 == 0:
        b += 1
        x //= 5
    return a, b, x

with open('27-A.txt', 'r', encoding='utf-8') as file:
    n = int(file.readline())

    l = [f(int(i)) for i in file.readlines()]

    l2 = [[0] * 8 for _ in range(8)]

    for i in l:
        l2[min(7, i[0])][min(7, i[1])] += 1
        
    print(f'n: {n}')
    print(*l2, sep='\n')

    pairs = 0

    for a in range(8):
        for b in range(8):
            for a2 in range(8):
                for b2 in range(8):
                    if min(a + a2, b + b2) == 6:
                        pairs += l2[a][b] * l2[a2][b2]
                        if a == a2 and b == b2:
                            pairs -= l2[a][b]
                            

    print(pairs // 2)
