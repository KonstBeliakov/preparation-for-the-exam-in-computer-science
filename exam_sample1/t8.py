n = 0

for i in range(8 ** 6, 8 ** 7):
    a = oct(i)[2:]

    evens = sum([1 for i in a if int(i) % 2 == 0])

    if evens == 2 and not any([int(a[i]) % 2 and int(a[i + 1]) == 7 for i in range(len(a) - 1)]) and \
            not any([int(a[i]) == 7 and int(a[i + 1]) % 2 for i in range(len(a) - 1)]):
        n += 1

print(n)
