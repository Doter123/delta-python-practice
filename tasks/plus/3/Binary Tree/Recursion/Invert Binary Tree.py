import sys
sys.path.append('../PrintTree')
sys.path.append('../CreateBinaryTree')
from PrintTree import PrintTree
from CreateBinaryTree import CreateTree, TreeNode
from typing import Optional

def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root: return None

    root.left, root.right = invertTree(root.right), invertTree(root.left)

    return root

root = CreateTree([4,2,7,1,3,6,9])
PrintTree(invertTree(root)) # [4,7,2,9,6,3,1]

root = CreateTree([2,1,3])
PrintTree(invertTree(root)) # [2,3,1]

root = CreateTree([])
PrintTree(invertTree(root)) # []
