d = (7, 68)
c = (29, 100)

for a0 in range(100):
    for a1 in range(100):
        for x in range(100):
            f = (d[0] <= x <= d[1]) <= ((not(c[0] <= x <= c[1]) and (not(a0 <= x <= a1))) <= (not(d[0] <= x <= d[1])))
            if not f:
                break
        else:
            print(a0, a1)

