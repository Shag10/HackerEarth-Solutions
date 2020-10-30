s = input()
s1 = []
for i in s:
    if i.islower():
        s1.append(i.upper())
    if i.isupper():
        s1.append(i.lower())

s1 = "".join(s1)
print(s1)
