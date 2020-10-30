import math

t = int(input())
for _ in range(t):
    a,b,c = list(map(int, input().split()))
    if((b-a)-(c-b)==0):
        print("0")
    else:
        print(math.ceil(abs((b-a)-(c-b))/2))
