numRows = 5
result = []

for i, n in enumerate(range(numRows)):
    temp_array = [1]
    if i > 1:
        for j in range(i - 1):
            first_num = result[i - 1][j]
            second_num = result[i - 1][j + 1]
            temp_array.append(first_num + second_num)

    if i != 0:
        temp_array.append(1)

    result.append(temp_array)

print(result)