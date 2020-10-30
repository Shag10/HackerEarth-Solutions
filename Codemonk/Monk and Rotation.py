t = int(input())
for _ in range(t):
    n, k = map(int, input().strip().split(" "))
    a = list(map(int, input().strip().split(" ")))
    k = k%n
    a = a[n-k:] + a[:n-k]
    print(*a)
