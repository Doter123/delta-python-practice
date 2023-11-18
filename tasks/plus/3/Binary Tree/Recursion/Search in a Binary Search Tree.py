import sys
sys.path.append('../PrintTree')
sys.path.append('../CreateBinaryTree')
from PrintTree import PrintTree
from CreateBinaryTree import CreateTree, TreeNode
from typing import Optional

def searchBST(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

    if not root: return None

    if root.val == val: return root

    if val < root.val:
        return searchBST(root.left, val)
    else:
        return searchBST(root.right, val)

root = CreateTree([4,2,7,1,3])

PrintTree(root)
PrintTree(searchBST(root, 2))
PrintTree(searchBST(root, 5)) 