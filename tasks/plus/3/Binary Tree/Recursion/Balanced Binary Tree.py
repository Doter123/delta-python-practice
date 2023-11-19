import sys
sys.path.append('../PrintTree')
sys.path.append('../CreateBinaryTree')
from PrintTree import PrintTree, bcolors
from CreateBinaryTree import CreateTree, TreeNode
from typing import Optional

def isBalanced(root: Optional[TreeNode]) -> bool:

    def helper(root):
        if not root:
            return True, 0

        left_bool, left_depth = helper(root.left)
        right_bool, right_depth = helper(root.right)

        if not left_bool or not right_bool:
            return False, -1

        return abs(left_depth - right_depth) < 2, 1 + max(left_depth, right_depth)

    return helper(root)[0]

root = CreateTree([3,9,20,None,None,15,7])
PrintTree(root)
bcolors.Test(isBalanced(root), True)

root = CreateTree([1,2,2,3,3,None,None,4,4])
PrintTree(root)
bcolors.Test(isBalanced(root), False)

root = CreateTree([])
PrintTree(root)
print(root)
bcolors.Test(isBalanced(root), True)

root = CreateTree([1,None,2,None,3])
PrintTree(root)
bcolors.Test(isBalanced(root), False)

root = CreateTree([1,2,3,4,5,6,None,8])
PrintTree(root)
bcolors.Test(isBalanced(root), True)

root = CreateTree([1,2,2,3,None,None,3,4,None,None,4])
PrintTree(root)
bcolors.Test(isBalanced(root), False)
