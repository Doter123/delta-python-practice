import sys
sys.path.append('../PrintTree')
from PrintTree import PrintTree
sys.path.append('../CreateBinaryTree')
from CreateBinaryTree import CreateTree, TreeNode

from typing import Optional
from collections import deque


def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if not p and not q: return True
    if not p or not q: return False
    
    return p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)


tree = CreateTree([1, 2, 3, 4, 5])
PrintTree(tree)

tree2 = CreateTree([1, 2, 3, 4, 5])
PrintTree(tree2)

print(isSameTree(tree, tree2))

tree3 = CreateTree([1, 2, 3, 4, 5, 6])
PrintTree(tree3)

print(isSameTree(tree, tree3))