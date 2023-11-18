import sys
sys.path.append('../PrintTree')
sys.path.append('../CreateBinaryTree')
from PrintTree import PrintTree
from CreateBinaryTree import CreateTree, TreeNode
from typing import Optional, List
from collections import deque


def averageOfLevels(root: Optional[TreeNode]) -> List[float]:

    ans = []

    q = deque([root])

    while q:

        summ = 0
        cnt = 0

        for _ in range(len(q)):

            cur = q.popleft()
            summ += cur.val
            cnt += 1

            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)

        ans.append(summ/cnt)

    return ans



# root = CreateTree([3,9,20,None,None,15,7])
# print(averageOfLevels(root)) # True

# root = CreateTree([3,9,20,15,7])
# print(averageOfLevels(root)) # False

# root = CreateTree([1,1])
# print(averageOfLevels(root)) # False

root = CreateTree([3,1,5,0,2,4,6])
PrintTree(root)
print(averageOfLevels(root)) # False
