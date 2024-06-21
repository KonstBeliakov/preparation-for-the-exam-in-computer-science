# 26_68259

# не работает

filename = '26_68259.txt'

with open(filename, 'r', encoding='utf-8') as file:
    n = file.readline()

    l = [[int(i.split()[0]), int(i.split()[1])] for i in file.readlines()]

    events = []
    for i in l:
        events.append([i[0], 'add'])
        events.append([i[1], '_remove'])

    threads = 0
    max_threads = 0
    time = 0  # max threads time

    start_time = 8 * 60 * 60  # 8:00
    end_time = 14 * 60 * 60   # 14:00

    events.append([start_time, 'start'])
    events.append([end_time, 'end'])
    
    events.sort()
    
    for i, event in enumerate(events): 
        match event[1]:
            case 'add':
                threads += 1
                if event[0] > start_time:
                    max_threads = max(threads, max_threads)
            case '_remove':
                if threads == max_threads:
                    time += events[i][0] - events[i - 1][0]
                threads -= 1
            case 'start':
                max_threads = max(max_threads, threads)
            case 'end':
                if threads == max_threads:
                    time += events[i][0] - events[i - 1][0]
                break

    print(f'max_threads: {max_threads}')
    print(f'max threads time: {time}')

    
