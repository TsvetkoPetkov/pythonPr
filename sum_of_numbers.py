number = int(input())

a = number

convert_to_string = str(a)
total_sum = 0
output = ''

for i in range(1, number+1):
    b = convert_to_string * i
    convert_to_int = int(b)
    total_sum += convert_to_int
    output += b + " + "

output_two = output[:-2]
print(output_two, end='')
print(f"= {total_sum}")
