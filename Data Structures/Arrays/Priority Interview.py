n = int(input())
gen = []
skill = []
for i in range(n):
    a,b = list(map(int, input().split()))
    gen.append(a)
    skill.append(b)

l = []
l2 = []
for j in range(len(gen)):
    if gen[j] == 0:
        l.append(skill[j])
    if gen[j] == 1:
        l2.append(skill[j])

l.sort(reverse = True)
l2.sort(reverse = True)
l.extend(l2)
l = " ".join(map(str, l))
print(l)
