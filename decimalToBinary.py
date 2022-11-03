print('Въведи число: ')
number = int(input())

print('Въведи бит: ')
bit = int(input())

str = ''

while number > 0:
    if number % 2 == 1:
        str += '1'
    else:
        str += '0'
    number = number//2

print('Числото в двуична бройна система: ')
print(str[::-1])

if str[::-1][bit - 1] == '1':
    print('yes')
else:
    print('no')





