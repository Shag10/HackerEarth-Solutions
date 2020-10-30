t = int(input())
for _ in range(t):
    n = int(input())
    ar = list(map(int, input().split()))
    x = 0
    for i in range(n):
        x^=ar[i]
    max1 = x
    y = 0
    z = 0
    for i in range(n):
        y^=ar[i]
        z = y&(y^x)

        if z > max1:
            max1 = z

    print(max1)
