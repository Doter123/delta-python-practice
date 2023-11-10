# Учитывая две строки 's' и 't', возвращайте 'true' значение, если они равны, при этом '#' означает символ возврата (backspace).
# То есть каждый '#' обозначает что предыдущий символ будет стёрт

def backspaceCompare(s: str, t: str) -> bool:
        
    def typing(string):
        stack = []

        for char in string:
            if char == '#':
                if stack: stack.pop()
            else: stack.append(char)

        return ''.join(stack)

    return typing(s) == typing(t)

print(backspaceCompare("ab#c", "ad#c")) # True
print(backspaceCompare("ab##", "c#d#")) # True
print(backspaceCompare("a#c", "b")) # False
print(backspaceCompare("xywrrmp", "xywrrmu#p")) # True