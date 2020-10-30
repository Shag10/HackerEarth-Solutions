t = int(input())
for _ in range(t):
    x,y = list(map(int, input().split()))
    if(x >= y and x >= 0 and y >= 0):
        print(x)
    elif(x < y or x < 0 or y < 0):
        print(-1)
