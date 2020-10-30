t = int(input())
for _ in range(t):
    a,b = list(map(int, input().split()))
    r = min(a,b)
    count = max(a,b)//r
    print(count)
