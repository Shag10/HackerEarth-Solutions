t = int(input())
for _ in range(t):
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])

    if (m%n == 0):
        print("Yes")
    else:
        print("No")
