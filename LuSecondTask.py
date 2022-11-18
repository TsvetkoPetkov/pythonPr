import random

s = []
n = int(input())
n_sum = 0

for i in range(n):
    number_one = random.randint(1, 40)
    s.append(number_one)
    number_two = random.randint(1, 40)
    n_sum = number_one + number_two
    s.append(n_sum)
    s.append(number_two)

print(s)
