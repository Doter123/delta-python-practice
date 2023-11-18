import sys
sys.path.append('../PrintTree')
sys.path.append('../CreateBinaryTree')
from PrintTree import PrintTree
from CreateBinaryTree import CreateTree, TreeNode
from typing import Optional


def rangeSumBST(root: Optional[TreeNode], low: int, high: int) -> int:

    if not root: return 0

    left, right = 0, 0

    if root.val < high:
        right = rangeSumBST(root.right, low, high)
    if root.val > low:
        left = rangeSumBST(root.left, low, high)

    current = root.val if low <= root.val <= high else 0

    return left + right + current


root = CreateTree([10,5,15,3,7,None,18])

PrintTree(root)
print(rangeSumBST(root, 7, 15)) # 32

root = CreateTree([10,5,15,3,7,13,18,1,None,6])

PrintTree(root)
print(rangeSumBST(root, 6, 10)) # 23