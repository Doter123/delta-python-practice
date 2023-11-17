def removeOuterParentheses(string: str) -> str:

    openCount = 0
    output = ""

    for char in string:
        if char == ")": openCount -= 1
        if openCount > 0: output += char
        if char == "(": openCount += 1

    return output

print(removeOuterParentheses("(()())(())")) # "()()()"
print(removeOuterParentheses("(()())(())(()(()))")) # "()()()()(())"
print(removeOuterParentheses("()()")) # ""