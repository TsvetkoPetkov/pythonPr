number = int(input())

a = number

convert_to_string = str(a)
total_sum = 0

for i in range(1, number+1):
    b = convert_to_string * i
    print(b)
    convert_to_int = int(b)
    total_sum += convert_to_int

print(total_sum)


