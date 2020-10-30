t = int(input())
for _ in range(t):
    l = []
    s = input()
    for i in s:
        if len(l) > 0 and i == l[0]:
            l.pop(0)
        else:
            l.insert(0,i)
    l.reverse()
    if len(l) != 0:
        print("".join(l))
    else:
        print("KHALI")
