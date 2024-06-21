with open('24_1.txt', 'r', encoding='utf-8') as file:
    text = 'ABCDABC'#file.read()

    sep = ['ABC', 'ACB', 'BCA', 'BAC', 'CAB', 'CBA']

    l = [-1]
    for i in range(len(text) - 2):
        if text[i:i + 3] in sep:
            l.append(i)
    dist = 0
    for i in range(len(l) - 1):
        dist = max(dist, l[i + 1] - l[i])
    print(dist - 3)
    
