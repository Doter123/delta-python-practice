
# charecter.isalnum() - Проверяет, что строка состоит только из цифр и буквенных символов

# Буквенно-цифровые символы включают буквы и цифры.
# Фраза является палиндромом,
# если после преобразования всех заглавных букв в строчные и удаления всех небуквенно-цифровых символов она читается одинаково и вперед, и назад.

# Дана строка, если это палиндром верните True или False если нет.

def isPalindrome(string: str) -> bool:
    left = 0
    right = len(string)-1
    while left <= right: # с двух сторон в центр пробегаемся
        if not string[left].isalnum(): # если это не небуквенно-цифровой символ
            left += 1 # увеличиваем индекс
            continue
        if not string[right].isalnum():
            right -= 1
            continue
        if string[left].lower() != string[right].lower():
            return False
        
        left += 1
        right -= 1

    return True


print(isPalindrome("A man, a plan, a canal: Panama")) # True

print(isPalindrome("race a car")) # False
