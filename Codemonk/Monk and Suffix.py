n,k = list(map(int, input().split()))
s = input()
l = [] 
for i in range(len(s)):
    x = s[i:]
    l.append(x)
 l = sorted(l)
 print(l[k-1])
    
