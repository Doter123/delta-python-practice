# Fibonacci Sequence = 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
# Numbers:             0, 1, 2, 3, 4, 5, 6, 7,  8,  9

# Число фибаначи равна сумме двух предидущих чисел фибаначи, верните число фибаначи

# @lru_cache(None)
def fib(n: int) -> int:
    if n < 2: return n
    return fib(n-1) + fib(n-2)

print(fib(0)) # 0
print(fib(1)) # 1
print(fib(2)) # 1
print(fib(3)) # 2
print(fib(4)) # 3
print(fib(5)) # 5
print(fib(6)) # 8
print(fib(7)) # 13
print(fib(8)) # 21
print(fib(9)) # 34