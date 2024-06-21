with open('27883.txt', 'r', encoding='utf-8') as file:
    s, n = file.readline().split()
    s = int(s)
    n = int(n)

    l = sorted([int(i) for i in file.readlines()])
    
    size = 0
    p = 0
    max_file_size = 0
    for i in l:
        if size + i > s:
            break
        max_file_size = max(i, max_file_size)
        size += i
        p += 1

    for i in l[::-1]:
        if size + i - l[0] <= s:
            max_file_size = max(i, max_file_size)

    print(f'max_file_size:{max_file_size}')
    print(f'size:{size}', f'p:{p}')
    
