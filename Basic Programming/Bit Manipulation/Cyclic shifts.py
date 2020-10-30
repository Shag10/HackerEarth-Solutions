t = int(input())
for _ in range(t):
    n,m,c = input().split()
    n = int(n)
    m = int(m)
    b = bin(n)
    b = b[2:].zfill(16)
    if c == 'R':
        a = b[-m:] + b[:-m]

    if c == 'L':
        a = b[m:] + b[:m]

    dec = str(a)
    print(int(dec,2))
