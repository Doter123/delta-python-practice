def addBinary(a: str, b: str) -> str:
    la, lb = len(a), len(b)

    if la > lb:
        b = '0' * (la - lb) + b
    else:
        a = '0' * (lb - la) + a

    carry = 0

    ans = ''

    for i in range(len(a)-1, -1, -1):
        d1 = int(a[i])
        d2 = int(b[i])

        carry, d = divmod(d1 + d2 + carry, 2)

        ans += str(d)

    if carry:
        ans += str(carry)

    return ans[::-1]
    # return bin(int(a, 2) + int(b, 2))[2:]

print(addBinary("11", "1"))
print(addBinary("1010", "1011"))