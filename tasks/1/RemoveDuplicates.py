numbers = [1,1,2,3,3,4,5,5,5,5,6,7,8,8,9,10,10]

i = 0
print(len(numbers))
while i != len(numbers) - 1:
    if numbers[i] == numbers[i + 1]:
        del numbers[i]
    else:
        i += 1
    
print(len(numbers), numbers)





result = set()

for number in numbers:
    result.add(number)

print(len(list(result)), list(result))