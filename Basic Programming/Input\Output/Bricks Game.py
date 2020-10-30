n = int(input())
c = 0
for i in range(n):
    c += i
    if(c>=n):
        print("Patlu")
        break

    c += 2*i
    if(c>=n):
        print("Motu")
        break
