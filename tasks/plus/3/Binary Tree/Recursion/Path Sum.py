import sys
sys.path.append('../PrintTree')
sys.path.append('../CreateBinaryTree')
from PrintTree import PrintTree
from CreateBinaryTree import CreateTree, TreeNode

from typing import Optional

def hasPathSum(root: Optional[TreeNode], targetSum: int) -> bool:
    hasPathSum = False
    def getPathSum(root, pathSum):
        nonlocal hasPathSum
        if not root: return
        pathSum += root.val
        if root.left:
            getPathSum(root.left, pathSum)
        if root.right:
            getPathSum(root.right, pathSum)
        elif not root.left and pathSum == targetSum:
            print(pathSum, targetSum)
            hasPathSum = True

    getPathSum(root, 0)
    return hasPathSum




tree = CreateTree([5,4,8,11,None,13,4,7,2,None,None,None,1])
PrintTree(tree)
print(hasPathSum(tree, 22))