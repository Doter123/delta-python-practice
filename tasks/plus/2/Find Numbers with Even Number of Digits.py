# Найдите числа с четным числом цифр.

nums = [12,345,2,6,7896] # Следовательно, только 12 и 7896 содержат четное количество цифр.

def findNumbers(self, nums: List[int]) -> int:
    def d_num(num):
        ret = 0
        while num:
            num //= 10
            ret += 1
        return ret

    ans = 0

    for num in nums:
        ans += 0 if d_num(num) % 2 else 1

    return ans # 2


# Short =====================

def findNumbers(self, nums: List[int]) -> int:
    ans = 0

    for num in nums:
        ans += 0 if len(str(num)) % 2 else 1

    return ans