n,m = input().split()
n = int(n)
m = int(m)
mat = {}
for i in range(int(n)):
    mat[i] = input()
c = 0 
for x in range(int(n)):
    for y in range(int(m)):
        if(mat[x][y]=='s'):
                if((x<(n-3)) and (mat[x+1][y]=='a' and mat[x+2][y]=='b' and mat[x+3][y]=='a')):
                        c += 1
                if((y<m-3) and (mat[x][y+1]=='a' and mat[x][y+2]=='b' and mat[x][y+3]=='a')):
                        c += 1
                if((x>=3 and y<(m-3)) and (mat[x-1][y+1]=='a' and mat[x-2][y+2]=='b' and mat[x-3][y+3]=='a')):
                        c += 1
                if((x<(n-3)and y<(m-3)) and (mat[x+1][y+1]=='a' and mat[x+2][y+2]=='b' and mat[x+3][y+3]=='a')):
                        c += 1                  

print(c)
