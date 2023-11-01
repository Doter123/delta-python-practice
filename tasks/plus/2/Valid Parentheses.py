# https://leetcode.com/problems/valid-parentheses/description/

# Учитывая строку string, содержащую только символы '(', ')', '{', '}', '[' и ']', определите, является ли входная строка допустимой.

# Входная строка действительна, если:

# Открытые скобки должны закрываться скобками того же типа.
# Открытые скобки должны закрываться в правильном порядке.

string = '()[]{}'

opened = []
close_to_open = {
    ')': '(',
    ']': '[',
    '}': '{',
}

for i in range(len(string)):
    char = string[i]
    if char == '(' or char == '{' or char == '[':
        opened.append(char)
    else:
        if opened[-1] == close_to_open[char]:
            opened.pop()
        else:
            break


print(len(opened) == 0)