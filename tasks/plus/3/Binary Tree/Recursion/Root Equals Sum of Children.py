import sys
sys.path.append('../PrintTree')
sys.path.append('../CreateBinaryTree')
from PrintTree import PrintTree, bcolors
from CreateBinaryTree import CreateTree, TreeNode
from typing import Optional

def checkTree(root: Optional[TreeNode]) -> bool:

    summ = 0

    def bfs(root):
        nonlocal summ
        if not root: return
        summ += root.val
        bfs(root.left)
        bfs(root.right)

    bfs(root.left)
    bfs(root.right)
    return summ == root.val



root = CreateTree([10,4,6])
PrintTree(root)
bcolors.Test(checkTree(root), True)


root = CreateTree([5,3,1])
PrintTree(root)
bcolors.Test(checkTree(root), False)