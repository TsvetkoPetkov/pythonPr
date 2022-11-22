n = int(input())
print("Въведи 0 или 1:")
zero_or_one = int(input())
s = []
s2 = []
print("Числа от списъка:")
for i in range(n):
    numbers = int(input())
    s.append(numbers)
    if zero_or_one == 0:
        if i % 2 == 0:
            s2.append(s[i] + 5)
        else:
            s2.append(numbers)
    elif zero_or_one == 1:
        if i % 2 == 1:
            s2.append(s[i] + 10)
        else:
            s2.append(numbers)
print("Начален списък:")
print(s)
print("Списък след действия:")
print(s2)







