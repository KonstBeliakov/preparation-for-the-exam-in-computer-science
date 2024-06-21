with open('26_41001.txt', 'r', encoding='utf-8') as file:
    n = int(file.readline())

    start_time = 1634515200
    end_time = start_time + 604800

    l = [[int(i.split()[0]), int(i.split()[1])] for i in file.readlines()]

    l2 = []
    for i in l:
        if end_time > i[0]:
            l2.append([i[0], 'add'])
        if end_time > i[1] and i[1] != 0:
            l2.append([i[1], 'remove'])

    l2.append([start_time, None])

    l2.sort()

    t = 0
    max_t = 0
    time = 0

    for i in range(len(l2)):
        if l2[i][1] == 'add':
            t += 1
            if t > max_t and l2[i][0] > start_time:
                max_t = t
        elif l2[i][1] == 'remove':
            t -= 1
        else:
            max_t = max(t, max_t)

    t = 0
    for i in range(len(l2)):
        if l2[i][1] == 'add':
            t += 1
        elif l2[i][1] == 'remove':
            t -= 1

        if l2[i][0] > end_time and t == max_t:
            time += end_time - l2[i - 1][0]

        if t == max_t and l2[i][0] > start_time:
            dt = min(l2[i][0], end_time) - max(start_time, l2[i - 1][0])
            time += dt
            print(l2[i][0], l2[i - 1][0], max(start_time, l2[i - 1][0]), dt)

    print(f'start time: {start_time} end_time: {end_time}')
    print(f'max threads: {max_t}')
    print(f'time: {time}')
    
    
