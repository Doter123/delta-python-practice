import sys
sys.path.append('../PrintTree')
sys.path.append('../CreateBinaryTree')
from PrintTree import PrintTree
from CreateBinaryTree import CreateTree, TreeNode
from typing import Optional


def findTarget(root: Optional[TreeNode], k: int) -> bool:
    seen = set()
    
    # def bfs(root, val):

    #     if val != None: seen.add(val)
    #     if not root: return False

    #     return (k - root.val in seen) or bfs(root.left, root.val) or bfs(root.right, root.val)

    # return bfs(root, None)

    stack = [root]

    while stack:
        current = stack.pop()

        if k - current.val in seen:
            return True
        seen.add(current.val)

        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)

    return False



root = CreateTree([5,3,6,2,4,None,7])
print(findTarget(root, 9)) # True

root = CreateTree([5,3,6,2,4,None,7])
print(findTarget(root, 28)) # False

root = CreateTree([1])
print(findTarget(root, 2)) # False

root = CreateTree([2,1,3])
print(findTarget(root, 1)) # False
