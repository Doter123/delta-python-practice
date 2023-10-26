result = 0
number = 8

left = 0
right = number
middle = (left + right) // 2

while(True):

    old_middle = middle

    if middle * middle > number:
        right = middle + 1

    else:
        left = middle

    middle = (left + right) // 2

    if old_middle == middle:
        break

result = left


print(1 if number == 1 else result)
print(int(pow(number, .5)))
print(int(number ** .5))




















































