a = []
n = int(input())
for _ in range(n):
    a.append(input())
for i in range(n):
    c = 0
    for j in range(0, i+1):
        if a[j] < a[i]:
            c += 1
    print(c)
