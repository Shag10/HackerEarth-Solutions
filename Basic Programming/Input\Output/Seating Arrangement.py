t = int(input())
for i in range(t):
    ans=0
    a = int(input())
    c = (a // 6)
    if c % 2 == 0:
        if a % 6 == 0:
            ans = (str(a - 11)+' ' +'WS')
        elif a % 6 == 1:
            ans = (str(a + 11)+' '+  'WS')
        elif a % 6 == 2:
            ans = (str(a + 9)+' '+ 'MS')
        elif a % 6 == 3:
            ans = (str(a + 7)+' '+ 'AS')
        elif a % 6 == 4:
            ans = (str(a + 5)+' '+ 'AS')
        elif a % 6 == 5:
            ans = (str(a + 3)+' '+ 'MS')

    if c % 2 != 0:
        if a % 6 == 0:
            ans = (str(a + 1)+' '+ 'WS')
        if a % 6 == 1:
            ans = (str(a - 1)+' '+ 'WS')
        if a % 6 == 2:
            ans = (str(a - 3)+' '+ 'MS')
        if a % 6 == 3:
            ans = (str(a - 5)+' '+ 'AS')
        if a % 6 == 4:
            ans = (str(a - 7)+' '+ 'AS')
        if a % 6 == 5:
            ans = (str(a - 9)+ ' ' +'MS')
    print(ans)
