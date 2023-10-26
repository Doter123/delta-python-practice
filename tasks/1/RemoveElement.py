numbers = [3,2,2,3,4,2]
value = 3

result = []

for num in numbers:
	if num != value:
		result.append(num)

print(len(result), result)

numbers = [i for i in numbers if i != value]

print(len(numbers), numbers) # 4 [2, 2, 4, 2]



while value in numbers:
	numbers.remove(value)

print(len(numbers), numbers) # 4 [2, 2, 4, 2]