def isHappy(n: int) -> bool:
    stack = set()
    while n != 1:
        n = sum([int(i)**2 for i in str(n)])
        if n in stack: return False
        stack.add(n)
    return True

print(isHappy(19)) # True
print(isHappy(2)) # False
