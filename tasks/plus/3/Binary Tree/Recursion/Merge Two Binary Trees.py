import sys
sys.path.append('../PrintTree')
from PrintTree import PrintTree
sys.path.append('../CreateBinaryTree')
from CreateBinaryTree import CreateTree, TreeNode

from typing import Optional, List
from collections import deque 

def mergeTrees(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

    if not root1: return root2
    if not root2: return root1

    result = TreeNode(root1.val + root2.val)

    result.left = mergeTrees(root1.left, root2.left)
    result.right = mergeTrees(root1.right, root2.right)

    return result

    
root1 = CreateTree([1,3,2,5])
PrintTree(root1)

root2 = CreateTree([2,1,3,None,4,None,7])
PrintTree(root2)

PrintTree(mergeTrees(root1, root2))