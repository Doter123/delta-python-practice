import sys
sys.path.append('../PrintTree')
sys.path.append('../CreateBinaryTree')
from PrintTree import PrintTree, bcolors
from CreateBinaryTree import CreateTree, GetTreeLevels, TreeNode
from typing import Optional

def increasingBST(root: TreeNode) -> TreeNode:
    def bfs(root):
        if not root: return []
        return [root.val] + bfs(root.left) + bfs(root.right)
    stack = sorted(bfs(root), key=None, reverse=True)

    current = TreeNode(None)
    result = current

    while stack:
        current.right = TreeNode(stack.pop())
        current = current.right

    return result.right


root = CreateTree([5,3,6,2,4,None,8,1,None,None,None,7,9])
PrintTree(root)
bcolors.Test(GetTreeLevels(increasingBST(root)), [1,None,2,None,3,None,4,None,5,None,6,None,7,None,8,None,9])


root = CreateTree([5,1,7])
PrintTree(root)
bcolors.Test(GetTreeLevels(increasingBST(root)), [1,None,5,None,7])
