# Цикл связанных списков
# Определите, есть ли в связанном списке цикл.


from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def getList(self, maxLength: int or None = None):
        stack = []

        if maxLength != None: i = 0

        node = self

        while node:
            stack.append(node.val)
            node = node.next
            if maxLength != None: i += 1
            if maxLength != None and i > maxLength: break

        return stack

    def hasCycle(self) -> bool:
        seen = set()

        node = self

        while node:
            if node in seen:
                return True
            seen.add(node)
            node = node.next

        return False

    def reverseList(self):

        prev = None
        current = self

        while current:
            current.next, prev, current = prev, current, current.next

        return prev

def createList(array: List):
    temp_list = ListNode(array[0])
    result = temp_list

    for value in array[slice(1, len(array))]:
        temp_list.next = ListNode(value)
        temp_list = temp_list.next

    return result

values = [1,2,3,4,5]

temp_list_node = createList(values)
list_node = temp_list_node
print('ListNode is Cycle', list_node.hasCycle(), list_node.getList())
list_node = list_node.reverseList()
print('ListNode is reversed', list_node.getList())

list_node.next.next.next.next.next = list_node
print('ListNode is Cycle', list_node.hasCycle(), list_node.getList(len(values)))

print((6 & 1))
