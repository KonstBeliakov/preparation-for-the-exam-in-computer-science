# 24_35913

with open('24_35913.txt', 'r', encoding='utf-8') as file:
    min_line = file.readline()
    min_n = min_line.count('N')
    
    for line in file.readlines():
        if line.count('N') < min_n:
            min_n = line.count('N')
            min_line = line
    
    d = {}
    for i in min_line:
        d[i] = d.get(i, 0) + 1

    print(sorted(d.items(), key=lambda x: x[::-1])[-1])
    
