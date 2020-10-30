from collections import Counter
t = int(input())
for _ in range(t):
    s = input()
    t = input()

    s = Counter(s)
    t = Counter(t)

    c = s - t
    c2 = t - s
    c = c + c2
    count = 0
    for key,values in c.items():
        x = c.get(key)
        count += x

    print(count)
