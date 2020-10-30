t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    c = 0
    o = 0
    for i in a:
        if i%2 == 0:
            c += 1
        else:
            o += 1

    print(c*o)
