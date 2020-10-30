t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    l = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for i in range(len(s) - 1):
        if(len(s) <= 1):
            print("0")
        elif((s[i] not in l) and (s[i+1] in l)):
            count +=1

    print(count)
