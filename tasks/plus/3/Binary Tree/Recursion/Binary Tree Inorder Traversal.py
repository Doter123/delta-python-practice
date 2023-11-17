import sys
sys.path.append('../PrintTree')
from PrintTree import PrintTree
sys.path.append('../CreateBinaryTree')
from CreateBinaryTree import CreateTree, TreeNode

from typing import List, Optional
from collections import deque


def inorderTraversal(root: Optional[TreeNode]) -> List[int]:
    def inorder(root: Optional[TreeNode],res:List[int]):
        if root is None:
            return
        inorder(root.left,res)
        res.append(root.val)
        inorder(root.right,res)    

    
    res=[]
    inorder(root,res)
    return res


tree = CreateTree([1,9,2,3,2,7,6])
PrintTree(tree)
print(inorderTraversal(tree)) # [3, 9, 2, 1, 7, 2, 6]


tree = CreateTree([1,None,2,3])
PrintTree(tree)
print(inorderTraversal(tree)) # [1,3,2]
