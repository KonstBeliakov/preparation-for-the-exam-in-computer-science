n = 0

with open('17.txt', 'r', encoding='utf-8') as file:
    l = [int(i) for i in file.readlines()]

    m = max([i for i in l if len(str(abs(i))) == 5 and abs(i) % 10 == 3])

    for i in range(len(l) - 2):
        if '3' in str(l[i])[-1]+str(l[i + 1])[-1]+str(l[i + 2])[-1] and l[i] + l[i + 1] + l[i + 2] <= m:
            n += 1

print(n)
