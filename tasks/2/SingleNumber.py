
numbers = [4,1,2,1,2]

temp_object = {}

for n in numbers:
    if n in temp_object:
        temp_object[n] += 1
    else:
        temp_object[n] = 1

for i in temp_object:
    if temp_object[i] == 1:
        print(i)
        break
