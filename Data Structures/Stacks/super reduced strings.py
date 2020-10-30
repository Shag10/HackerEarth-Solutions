s = input()
l = []
for i in s:
    if len(l)>0 and i == l[0]:
        l.pop(0)
    else:
        l.insert(0,i)

if len(l) > 0:
    for i  in l[::-1]:
        print(i,end="")
else:
    print("Empty String")
