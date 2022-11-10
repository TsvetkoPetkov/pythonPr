number = int(input())
a = 0
b = 1
fibonacci_number = 0

for i in range(number+2):
    print(a)
    fibonacci_number = a + b
    a = b
    b = fibonacci_number
    i += 1

