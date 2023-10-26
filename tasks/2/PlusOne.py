numbers = [4,3,2,9]

string = ''

for number in numbers:
    string += str(number)

string = str(int(string) + 1)

result = []

for character in string:
    result.append(int(character))
















# Short
number=int("".join(map(str, numbers)))

number+=1

result = list(str(number))








print(result)
