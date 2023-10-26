number = 121

number = str(number)

number_clone = ''

for char in number:
    number_clone = char + number_clone

print(number == number_clone)




# Short Example

print(str(number) == str(number)[::-1])

print('самоходка'[4:1:-1]) # 'хом'
print('самоходка'[3:7:1]) # 'оход'
print('самоходка'[3:7:]) # 'оход'
print('самоходка'[2:7:2]) # 'мхд'