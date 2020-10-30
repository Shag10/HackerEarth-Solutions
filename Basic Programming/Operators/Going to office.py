d = int(input())
ocfd = input().split(" ")
oc = int(ocfd[0])
of = int(ocfd[1])
od = int(ocfd[2])
csbmd = input().split(" ")
cs = int(csbmd[0])
cb = int(csbmd[1])
cm = int(csbmd[2])
cd = int(csbmd[3])

otr = oc + (d - of)*od
ctr = cb + (d//cs)*cm + d*cd

if otr <= ctr:
    print("Online Taxi")
else:
    print("Classic Taxi")
