pie = 22/7
d = int(input())
tof = 0
while d>0:
    r,x = list(map(int, input().split()))
    enr = x*100
    cir = 2*pie*r
    l = []
    if enr >= cir:
        tof += 1

    d -= 1

print(tof)
