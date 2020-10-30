import math
t = int(input())
for _ in range(t):
    l,r,s = list(map(int, input().split()))
    st = math.ceil(l/s)
    en = r//s
    if st*s >= l and en*s <= r and en >= st:
        print(st, en)

    else:
        print(-1, -1)
        
