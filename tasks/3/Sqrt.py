result = 0
number = 8

left = 0
right = number
middle = (left + right) // 2

while(True):

    old_middle = middle

    print('old_middle', old_middle)
    print('result', middle * middle, 'number', number)

    if middle * middle > number:
        right = middle + 1
        print('right', right)
    else:
        left = middle
        print('left', left)

    middle = (left + right) // 2
    print('middle', middle)
    print('=============')

    if old_middle == middle:
        break

result = left


print(1 if number == 1 else result)

print(int(pow(number, .5)))
print(int(number ** .5))
