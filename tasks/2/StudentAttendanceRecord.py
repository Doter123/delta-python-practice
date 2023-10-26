string = "PPALLP"

result = True

absent_count = 0
late_count = 0

for char in string:
    if char == 'A':
        absent_count += 1
    if char == 'L':
        late_count += 1
    else:
        late_count = 0

    if late_count >= 3 or absent_count >= 2:
        result = False
        break

print(result)
print(string.count("A") < 2 and "LLL" not in string)