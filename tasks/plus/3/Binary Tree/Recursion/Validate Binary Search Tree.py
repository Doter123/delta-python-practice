import sys
sys.path.append('../PrintTree')
sys.path.append('../CreateBinaryTree')
from PrintTree import PrintTree, bcolors
from CreateBinaryTree import CreateTree, TreeNode
from typing import Optional

def isValidBST(root: Optional[TreeNode], min_val=float('-inf'), max_val=float('inf')) -> bool:
    if root == None: return True

    if not (min_val < root.val < max_val): return False

    return (
        isValidBST(root.left, min_val, root.val) and
        isValidBST(root.right, root.val, max_val)
    )



root = CreateTree([2,1,3])
PrintTree(root)
bcolors.Test(isValidBST(root), True)

root = CreateTree([5,1,4,None,None,3,6])
PrintTree(root)
bcolors.Test(isValidBST(root), False)

root = CreateTree([2,2,2])
PrintTree(root)
bcolors.Test(isValidBST(root), False)

root = CreateTree([0,-1])
PrintTree(root)
bcolors.Test(isValidBST(root), True)

root = CreateTree([5,4,6,None,None,3,7])
PrintTree(root)
bcolors.Test(isValidBST(root), False)