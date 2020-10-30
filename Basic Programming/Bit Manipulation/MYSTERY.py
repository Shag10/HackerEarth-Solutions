from sys import stdin

for n in stdin:

    if n == '':

        break

    print(str(bin(int(n))).count('1'))
