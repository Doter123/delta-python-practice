# https://leetcode.com/problems/valid-parentheses/description/

# Учитывая строку string, содержащую только символы '(', ')', '{', '}', '[' и ']', определите, является ли входная строка допустимой.

# Входная строка действительна, если:

# Открытые скобки должны закрываться скобками того же типа.
# Открытые скобки должны закрываться в правильном порядке.

string = '()[]{}' # True
# string = '{' # False
# string = '({)' # False
# string = '({]]' # False
# string = '([]{)}' # False
# string = '([]{)}' # False

stack = []
obj = {
    ')': '(',
    ']': '[',
    '}': '{',
}

for char in string:
    if char == '(' or char == '{' or char == '[':
        stack.append(char)
    elif stack[-1] == obj[char]:
        stack.pop()
    elif: return False


print(len(stack) == 0)