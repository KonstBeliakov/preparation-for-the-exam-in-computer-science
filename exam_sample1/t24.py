with open('24.txt', 'r', encoding='utf-8') as file:
    s = file.read()
s.replace('8', '9')
s.replace('A', 'C')
s.replace('B', 'C')

s += s[-1]

print(f'{len(s):_}')

start = 0
m = -10 ** 9

for i in range(1, len(s)):
    if i - start > m:
        m = i - start
    if s[i] == s[i - 1]:
        start = i

print(m)  # 60
