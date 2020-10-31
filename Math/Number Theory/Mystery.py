import math
n = int(input())
for _ in range(n):
    num = int(input())
    c = 0
    for i in range(2, int(math.sqrt(num)+1)):
        if num%i == 0:
            c += 1
            if num%(num/i) == 0 and i != (num/i):
                c += 1
    if num > 1:
        print(c + 2)
    else:
        print("1")
