numRows = 6
result = []

for index in range(numRows): # 0 ... -> 5

    temp_array = [1]

    if index > 1:
        last_level = result[index - 1]
        for j in range(len(last_level) - 1):
            first_num = last_level[j]
            second_num = last_level[j + 1]
            temp_array.append(first_num + second_num)

    if index != 0:
        temp_array.append(1)

    result.append(temp_array)

print(*result, sep='\n')
