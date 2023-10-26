




numbers = [10,7,5,3]

result = False

temp_set = set()

for num in numbers:

    if num * 2 in temp_set or num / 2 in temp_set:
        result = True

    temp_set.add(num)

print(result)















































