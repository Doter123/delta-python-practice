import sys
sys.path.append('../PrintTree')
from PrintTree import PrintTree
sys.path.append('../CreateBinaryTree')
from CreateBinaryTree import CreateTree, TreeNode

from typing import Optional
from collections import deque 

levels = [1, 2, 3, 4, 5]
tree = CreateTree(levels)
PrintTree(tree)

# def minDepth(root: Optional[TreeNode]) -> int:

#     if not root:
#         return 0

#     stack = []
#     def getLastRoots(root, index):
#         if not root: return
#         if root.left:
#             getLastRoots(root.left, index + 1)
#         if root.right:
#             getLastRoots(root.right, index + 1)
#         elif not root.left:
#             stack.append(index)

#     getLastRoots(root, 1)

#     return min(stack)



def minDepth(root: Optional[TreeNode]) -> int:

    if not root:
        return 0

    queue = deque([(root, 1)])

    while queue:
        current, depth = queue.popleft()

        if not current.left and not current.right:
            return depth

        if current.left:
            queue.append((current.left, depth+1))

        if current.right:
            queue.append((current.right, depth+1))

print('minDepth', minDepth(tree))



levels = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, None, None, None, None, 5, 6, 2, 4, 5]
new_tree = CreateTree(levels)
PrintTree(new_tree)
print('minDepth', minDepth(new_tree))
