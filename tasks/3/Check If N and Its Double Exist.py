numbers = [10,7,5,3]

result = False

for num in numbers:

    if num * 2 in numbers or num / 2 in numbers:
        result = True
        break


print(result)
