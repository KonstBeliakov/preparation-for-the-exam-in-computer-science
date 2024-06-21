with open('24_2792.txt', 'r', encoding='utf-8') as file:
    t = 0
    max_b = 0
    for i in file.read():
        if i == 'B':
            t += 1
        else:
            max_b = max(max_b, t)
            t = 0
    print(max_b)
