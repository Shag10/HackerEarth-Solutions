t = int(input())
for _ in range(t):
    n = int(input())
    sum1 = 1
    a = n&(n-1)
    b= bin(a)
    c = b.count('1')
    sum1 += c
    print(sum1) 
    
