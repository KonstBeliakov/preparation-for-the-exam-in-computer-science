# 27_40743

# переписанное в сокращенном (менее ужасном) виде решение из ответа

f = open("27_40743_B.txt")
n = int(f.readline())
lefts = [2 * 10 ** 9] * 30
maxsum = 0
count = 0
s = 0

for num in map(int, f.readlines()):
    s = s + num
    
    count += (num % 2 == 0) and (num > 0)

    d = count % 30

    lefts[d] = min(lefts[d], s)
        
    maxsum = max(maxsum, s - lefts[d])

print(maxsum)
