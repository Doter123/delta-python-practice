import sys
sys.path.append('../PrintTree')
sys.path.append('../CreateBinaryTree')
from PrintTree import PrintTree, bcolors
from CreateBinaryTree import CreateTree, TreeNode
from typing import Optional

def sumRootToLeaf(root: Optional[TreeNode], path = 0) -> int:
    if not root: return 0

    path = (path << 1) + root.val
    
    if not root.left and not root.right: return path
    
    return sumRootToLeaf(root.left, path) + sumRootToLeaf(root.right, path)


root = CreateTree([1,0,1,0,1,0,1])
PrintTree(root)
# Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
bcolors.Test(sumRootToLeaf(root), 22)


root = CreateTree([0])
PrintTree(root)
bcolors.Test(sumRootToLeaf(root), 0)