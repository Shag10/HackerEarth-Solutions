n = int(input())
for _ in range(n):
    num = int(input())
    l = []
    for i in range(1, num+1):
        if num%i == 0:
            l.append(i)
    l.pop()
    print(sum(l))
