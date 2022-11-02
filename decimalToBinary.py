print('Въведи число: ')
number = int(input())
str = ''

while number > 0:
    if number % 2 == 1:
        str += '1'
    else:
        str += '0'
    number = number//2

print('Числото в двуична бройна система: ')
print(str[::-1])

print('Има ли 1 на петия бит от числото: ')
if str[4] == '1':
    print('Yes')
else:
    print('No')