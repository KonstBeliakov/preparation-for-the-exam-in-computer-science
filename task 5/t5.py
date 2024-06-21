
for i in range(1, 100):
    a = int(bin(i)[2:][::-1], 2)
    if a == 13:
        print(i)