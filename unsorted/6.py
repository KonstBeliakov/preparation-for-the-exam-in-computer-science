with open('26.txt', 'r', encoding='utf-8') as file:
    a = 80
    b = 20
    
    n = int(file.readline())

    l = [[int(i.split()[0]), int(i.split()[1]), i.split()[2]] for i in file.readlines()]

    places = [None] * len(l)

    l2 = []
    for i, event in enumerate(l):
        l2.append({'command': 'add', 'time': event[0], 'type': event[2], 'number': i})
        l2.append({'command': 'remove', 'time': event[0] + event[1], 'type': event[2], 'number': i})

    l2 = sorted(l2, key=lambda x: x['time'])

    print(l2[:100])
    print(len(l))

    parked = 0
    not_parked = 0
    for i in l2:
        if i['command'] == 'add':
            if i['type'] == 'B' or a == 0:
                if b > 0:
                    b -= 1
                    if i['type'] == 'A':
                        parked += 1
                    places[i['number']] = 'B'
                else:
                    not_parked += 1
            else:
                if a > 0:
                    a -= 1
                    places[i['number']] = 'A'
                    parked += 1
                else:
                    not_parked += 1
        else: # i[0] == 'remove'
            if places[i['number']] == 'A':
                a += 1
            else:
                b += 1
    print(f'cars:{len(l)}')
    print(f'parked (only light cars): {parked}')
    print(f'not parked: {not_parked}')
