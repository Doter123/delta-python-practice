# numbers = [3,2,4]
# target = 6
# numbers = [3,3]
# target = 6
numbers = [2,7,11,15]
target = 9

for i, num in enumerate(numbers):
    if target - num in numbers and i != numbers.index(target - num):
        print(i, numbers.index(target - num))
        break