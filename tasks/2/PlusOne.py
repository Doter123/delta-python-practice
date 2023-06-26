numbers = [4,3,2,9]

string = ''

for number in numbers:
    string += str(number)

temp_number = int(string)
temp_number = temp_number + 1
string = str(temp_number)

result = []

for character in string:
    result.append(int(character))


# Short
# number=int("".join(map(str, numbers)))
# number+=1

# result = list(str(number))

print(result)
