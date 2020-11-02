from sys import stdin
def triangle(n):
    arr=[]
    num=0
    while(n):
        arr.append(n%9)
        n=n//9

    if arr:
        num=arr.pop()
        while(arr):
            num*=10
            num+=arr.pop()

    return num


 
for n in stdin:
    if n=='':
        break
    n=int(n)
    print(triangle(n))
