t = int(input())
for _ in range(t):
    n = int(input())
    a = []
    m = []
    l = []
    c = 0
    for _ in range(n):
        a.append(list(map(int, input().strip().split(" "))))
    for i in range(n):
        for j in range(n):
            m.append((i, j))
            l.append((i, j))
    for i, j in m:
        for p, q in l:
            if i <= p and j <= q:
                if a[i][j] > a[p][q]:
                    c += 1
    print(c)
