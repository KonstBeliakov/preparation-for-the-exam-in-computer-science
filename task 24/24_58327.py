# 24_58327

# плохое решение

filename = '24_58327.txt'

with open(filename, 'r', encoding='utf-8') as file:
    line = file.read()

answer = 0

for i in range(len(line)):
    j = i + 1
    while j < len(line) and line[j - 1] >= line[j]:
        j += 1
    if answer < j - i:
        answer = j - i
        print(line[i:j], answer)

print(answer)
