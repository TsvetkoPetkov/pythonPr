number = int(input())

s = []

for i in range(1, number+1):
    s.append(i)
print(s)
d = {}

rev_s = s.reverse()

for i in range(1, number+1):
    d[i] = s[i-1]

print(d)
