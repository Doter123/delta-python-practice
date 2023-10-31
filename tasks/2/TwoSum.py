numbers = [11,15,2,7]

target = 9

for i, num in enumerate(numbers):

    if target - num in numbers and i != numbers.index(target - num):

        print(i, numbers.index(target - num))

        break

for i, num in enumerate(numbers):

    if len(numbers) != i + 1 and numbers[i + 1] + num == target:

        print(i, numbers.index(target - num))

        break