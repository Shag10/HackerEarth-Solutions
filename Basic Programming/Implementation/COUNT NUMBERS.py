import re
t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    a = re.findall(r'\d+', s)
    l = list(map(int, a))
    print(len(l))
