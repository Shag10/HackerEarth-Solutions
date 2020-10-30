n = int(input())
a = list(map(int, input().split()))
max_a = max(a)
mul = 1
rem = 10**5
while max_a:
    a.sort(key = lambda x: (x/mul)%rem)
    print(" ".join(map(str, a)))
    mul *= rem
    max_a //= rem
