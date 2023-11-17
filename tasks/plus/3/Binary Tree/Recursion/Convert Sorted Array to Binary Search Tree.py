import sys
sys.path.append('../PrintTree')
from PrintTree import PrintTree
sys.path.append('../CreateBinaryTree')
from CreateBinaryTree import CreateTree, TreeNode

from typing import Optional, List
from collections import deque 

def sortedArrayToBST(nums: List[int]) -> Optional[TreeNode]:

    def helper(l: int, r: int):

        if l <= r:
            mid = (l + r) // 2

            root = TreeNode(nums[mid])

            root.left = helper(l, mid - 1)
            root.right = helper(mid + 1, r)

            return root

    return helper(0, len(nums)-1)

    

tree = CreateTree([0,-3,9,-10, None,5]) # the same = [-10,-3,0,5,9]
PrintTree(tree)
PrintTree(sortedArrayToBST([-10,-3,0,5,9]))