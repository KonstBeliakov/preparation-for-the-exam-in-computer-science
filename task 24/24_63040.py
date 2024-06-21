with open('24_63040.txt', 'r', encoding='utf-8') as file:
    text = file.read()

    l = [[-1, None]] + [[i, text[i]] for i in range(len(text)) if text[i] in ['A', 'B']]

    max_length = 0

    for i in range(len(l)):
        a = 0
        b = 0
        for j in range(i + 1, len(l)):
            a += l[j][1] == 'A'
            b += l[j][1] == 'B'
            
            #print(i, j, a, b)
            if a > 2 or b > 2:
                #print('aaa', l[i][0], l[j][0], l[j][0] - l[i][0] - 1)
                max_length = max(max_length, l[j][0] - l[i][0] - 1)
                break
        else:
            #print('aaa', l[i][0], None, len(text) - l[i][0] - 1)
            max_length = max(max_length, len(text) - l[i][0] - 1)
    #print(text)
    print(f'max_length: {max_length}')
