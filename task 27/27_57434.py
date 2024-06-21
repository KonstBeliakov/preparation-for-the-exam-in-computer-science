# 27_57434

with open('57434_B.txt', 'r', encoding='utf-8') as file:
    k = int(file.readline())
    n = int(file.readline())

    print(f'k: {k}, n: {n}')

    l = [int(i) for i in file.readlines()]

    max_pair_sum = 0

    max_in_k = max(l[k:])
    
    for i in range(len(l)):
        if l[i] + max_in_k > max_pair_sum:
            for j in range(i + k, len(l)):
                if l[i] + l[j] > max_pair_sum:
                    max_pair_sum = l[i] + l[j]
                    print(f'l[{i}]: {l[i]}, l[{j}]: {l[j]}, max_pair_sum: {max_pair_sum}')

    print(max_pair_sum)
