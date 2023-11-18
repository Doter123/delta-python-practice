from ListNodeCycle import ListNode, createList

def getDecimalValue(head: ListNode) -> int:

    # binary = ''

    # while head:
    #     binary += str(head.val)
    #     head = head.next

    # return int(int(binary, 2))

    result = 0

    while head:
        result = result * 2 + head.val
        head = head.next

    return result


print(getDecimalValue(createList([0])))
print(getDecimalValue(createList([1])))
print(getDecimalValue(createList([1,0])))
print(getDecimalValue(createList([1,1])))
print(getDecimalValue(createList([1,0,0])))
print(getDecimalValue(createList([1,0,1])))
print(getDecimalValue(createList([1,0,0,1,0,1])))
print(getDecimalValue(createList([0,1,0,0,1,0,1])))