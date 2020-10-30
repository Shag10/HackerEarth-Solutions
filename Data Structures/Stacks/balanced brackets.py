n = int(input())
for _ in range(n):
    s = input()
    l = []
    for i in s:
        if len(l)>0:
            if((l[0]=='{' and i=='}') or (l[0]=='(' and i==')') or (l[0]=='[' and i==']')):
                l.pop(0)
            else:
                l.insert(0,i)
        else:
            l.insert(0,i)

    if len(l) == 0:
        print("YES")
    else:
        print("NO")
