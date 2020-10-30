n = int(input())
ca = list(map(int, input().split()))
ideal = list(map(int, input().split()))
c = 0
for i in ideal:
    if i == ca[0]:
        ca.remove(i)
        c += 1
    else:
        ind = ca.index(i)
        ca = ca[ind:] + ca[:ind]
        ca.remove(i)
        c += ind + 1
print(c)
