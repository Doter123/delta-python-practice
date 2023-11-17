numRows = 6
result = []

# for index in range(numRows): # 0 ... -> 5

#     temp_array = [1]

#     if index > 1:
#         last_row = result[-1]
#         for j in range(len(last_row) - 1):
#             first_num = last_row[j]
#             second_num = last_row[j + 1]
#             temp_array.append(first_num + second_num)

#     if index != 0:
#         temp_array.append(1)

#     result.append(temp_array)

# print(*result, sep='\n')



# ===============================

triangle = [[1], [1,1]]

if numRows < 3:
    print(triangle[:numRows])

for _ in range(2, numRows):
    last_triangle = triangle[-1]
    new_row = [1]

    for i in range(1, len(last_triangle)):
        new_row.append(last_triangle[i-1] + last_triangle[i])
    new_row.append(1)

    triangle.append(new_row)
    
print(*triangle, sep='\n')
