rowIndex = 3
result = []

for index in range(rowIndex + 1):

    temp_array = [1]

    if index > 1:
        for j in range(index - 1):
            first_num = result[index - 1][j]
            second_num = result[index - 1][j + 1]
            temp_array.append(first_num + second_num)

    if index != 0:
        temp_array.append(1)

    result.append(temp_array)

print(result[rowIndex])



























