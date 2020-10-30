n,k = list(map(int, input().split()))
a = list(map(int, input().split()))
sl = 0
ss = 0
c = 0
for i in range(n):
    if i>=n-k:
        sl += a[i]
for i  in range(k):
    ss += a[i]
    sl -= a[n-k+i]
    if c < ss+sl:
        c = ss + sl
print(c)
