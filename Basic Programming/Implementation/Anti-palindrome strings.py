t = int(input())
for _ in range(t):
    s = input()
    if 2 <= len(s) <= (2*(10**5)):
        s1 = sorted(s)
        s3 = "".join(s1)

        s1.reverse()
        s2 = "".join(s1)
        if s3 == s2:
            print("-1")
        else:
            print(str(s3))
