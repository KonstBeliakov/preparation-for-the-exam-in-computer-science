
print('x y z w f')

def f(l):
    for x in 0, 1:
         for y in 0, 1:
             for z in 0, 1:
                 for w in 0, 1:
                     f1 = int(not((((not w) <= (not y)) <= (not z)) <= x))

                     if l(x, y, z, w, f1):
                         print(x, y, z, w, f1)
    print()

f(lambda x, y, z, w, f: f and 2 >= x + y + z + w >= 1 and not y)
f(lambda x, y, z, w, f: f and 3 >= x + y + z + w >= 2 and y)
f(lambda x, y, z, w, f: (not f) and 2 >= x + y + z + w >= 1 and not x and not y)