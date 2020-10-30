t = int(input())
for _ in range(t):
    n = int(input())
    while n>0:
        if n%2 == 0:
            n = n//2
            if n == 1:
                print("YES")
                break
            else:
                continue
        if n%2 == 1:
            n = 3*n + 1
            if n == 1:
                print("YES")
                break
            else:
                continue
