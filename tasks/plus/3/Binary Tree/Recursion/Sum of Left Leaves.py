import sys
sys.path.append('../PrintTree')
sys.path.append('../CreateBinaryTree')
from PrintTree import PrintTree
from CreateBinaryTree import CreateTree, TreeNode
from typing import Optional

def sumOfLeftLeaves(root: Optional[TreeNode]) -> int:
    leftLeaves = 0
    def sumLeftRoots(root: Optional[TreeNode], isLeft: bool):
        nonlocal leftLeaves
        if root.right:
            sumLeftRoots(root.right, False)
        if root.left:
            sumLeftRoots(root.left, True)
        elif isLeft and not root.right:
            leftLeaves += root.val

    sumLeftRoots(root, False)

    return leftLeaves

root = CreateTree([3,9,20,None,None,15,7])

print(sumOfLeftLeaves(root)) # 24
