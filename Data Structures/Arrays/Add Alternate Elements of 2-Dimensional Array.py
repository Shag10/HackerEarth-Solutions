ar = list(map(int, input().split()))
sum1 = 0
sum2 = 0
for i in range(len(ar)):
    if i%2 == 0:
        sum1 += ar[i]
    if i%2 != 0:
        sum2 += ar[i]

print(sum1)
print(sum2)
