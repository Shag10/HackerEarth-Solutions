n = int(input())
c = 0
while n > 0:
    if n == 4:
        n = n - 4
        c += 1
    elif n == 3:
        n = n - 3
        c += 1
    elif n == 2:
        n = n - 2
        c += 1
    elif n == 1:
        n = n - 1
        c += 1
    else:
        n = n - 5
        c += 1
print(c)
