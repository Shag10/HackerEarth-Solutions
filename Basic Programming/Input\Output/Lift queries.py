A = 0
B = 7
t = int(input())
for _ in range(t):
    n = int(input())
    if((B-n)<(n-A)):
        print("B")
        B = n

    elif((B-n) > (n-A)):
        print("A")
        A = n

    else:
        print("A")
        A = n
