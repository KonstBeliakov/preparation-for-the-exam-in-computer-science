with open('27-B.txt', 'r', encoding='utf-8') as file:
    k = int(file.readline())
    n = int(file.readline())

    l1 = [int(i) for i in file.readlines()]

    l, r = 0, 1
    m = 0

    s = l1[0]

    while r < len(l1):
        m = max(m, r - l)
        if s < k and s + l1[r] <= k:
            s += l1[r]
            r += 1
        else:
            s -= l1[l]
            l += 1

    print(m)
