n = int(input())
c = 0
for _ in range(n):
    y = int(input())
    if(y&(y-1) == 0):
        c += 1
print(c)
    
