n,q=map(int,input().split())

a=list(map(int,input().split()))

b=[a[0]]

for i in range(1,len(a)):
    b.append(a[i]+b[i-1])

for _ in range(q):
    l,r=map(int,input().split())

    if(l==1):
        ans=b[r-1]//(r-l+1)
    else:
        ans=(b[r-1]-b[l-2])//(r-l+1)

    print(ans)
