# Форматирование лицензионного ключа

def licenseKeyFormatting(s: str, k: int) -> str:
    s = s.replace("-", "").upper()
    
    ans = ''

    for i in range(len(s)-1,-1,-1):
        if not len(ans) % (k+1): # len('5F3Z-') = 5 % 5 = 0
            ans += '-'
        ans += s[i]
    
    return ans[::-1][:-1]

    # first_group_len = len(s) % k

    # reformatted = s[:first_group_len]

    # for i in range(first_group_len, len(s), k):
    #     if reformatted:
    #         reformatted += "-"
    #     reformatted += s[i:i+k]

    # return reformatted

print(licenseKeyFormatting("5F3Z-2e-9-w", 4)) # "5F3Z-2E9W"
print(licenseKeyFormatting("2-5g-3-J", 2)) # "2-5G-3J"