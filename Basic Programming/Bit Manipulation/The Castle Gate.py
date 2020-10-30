import itertools
t = int(input())
for _ in range(t):
    n = int(input())
    c = 0
    l = []
    for i in range(1, n+1):
        l.append(i)
    for i in itertools.combinations(l, 2):
        x = i[0]^i[1]
        if x<=n:
            c += 1

    print(c) 
