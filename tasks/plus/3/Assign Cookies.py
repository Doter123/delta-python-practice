# Надо выяснить сколько комнат с детьми мы можем полностью накормить (не оставив не одного в комнате без печенья)

# Ограничения: назначив ячейку для комнаты с детьми нельзя воспользоваться остатками печенбев из этой ячейки для других комнат с детьми


from typing import List

def findContentChildren(children: List[int], cookies: List[int]) -> int:

    children.sort()
    cookies.sort()

    # a = len(children) - 1
    # b = len(cookies) - 1
    # maxs = 0

    # while a >= 0 and b >= 0:
    #     if cookies[b] >= children[a]:
    #         maxs += 1
    #         a -= 1
    #         b -= 1
    #     else:
    #         a -= 1
    # return maxs

    i = 0

    for c in cookies:
        if c >= children[i]:
            i += 1

        if i == len(children): break

    return i

print(findContentChildren([1,2,3], [1,1])) # 1
print(findContentChildren([1,2], [1,2,3])) # 2
print(findContentChildren([1,2,3], [3])) # 1