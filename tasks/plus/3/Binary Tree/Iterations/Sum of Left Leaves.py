import sys
sys.path.append('../PrintTree')
sys.path.append('../CreateBinaryTree')
from PrintTree import PrintTree
from CreateBinaryTree import CreateTree, TreeNode
from typing import Optional

def sumOfLeftLeaves(root: Optional[TreeNode]) -> int:
    leftLeaves = 0

    stack = [(root, False)]

    while stack:
        current, isLeft = stack.pop()

        if isLeft and not current.left and not current.right:
            leftLeaves += current.val

        if current.right:
            stack.append((current.right, False))
        if current.left:
            stack.append((current.left, True))


    return leftLeaves

root = CreateTree([3,9,20,None,None,15,7])

print(sumOfLeftLeaves(root)) # 24
