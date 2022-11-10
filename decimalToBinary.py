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

print('Числото в двоична бройна система: ')
new_str = str[::-1]
print(new_str)

if str[bit] == '1':
    print('yes')
else:
    print('no')






