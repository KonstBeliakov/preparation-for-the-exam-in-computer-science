print(sum([all([set(i[j:j+3]) & set('мнгд') for j in range(len(i) - 2)]) for i in __import__('itertools').permutations('мнегода', 7)]))