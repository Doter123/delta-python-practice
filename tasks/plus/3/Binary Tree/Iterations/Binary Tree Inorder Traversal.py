from sys import path
path.append('../PrintTree')
path.append('../CreateBinaryTree')
from PrintTree import PrintTree
from CreateBinaryTree import CreateTree, TreeNode
from typing import List, Optional


def inorderTraversal(root: Optional[TreeNode]) -> List[int]:
    result = []
    stack = []

    while stack or root:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        result.append(root.val)
        root = root.right

    return result


tree = CreateTree([1,9,2,3,2,7,6])
PrintTree(tree)
print(inorderTraversal(tree)) # [3, 9, 2, 1, 7, 2, 6]


tree = CreateTree([1,None,2,3])
PrintTree(tree)
print(inorderTraversal(tree)) # [1,3,2]
