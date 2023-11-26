import sys
sys.path.append('../PrintTree')
sys.path.append('../CreateBinaryTree')
from PrintTree import PrintTree, bcolors
from CreateBinaryTree import CreateTree, TreeNode
from typing import Optional, List

def levelOrderBottom(root: Optional[TreeNode]) -> List[List[int]]:
    
    if not root: return []
    stack = [[root.val]]

    def bfs(root, i = 1):
        nonlocal stack

        temp = []
        if not root: return

        if root.left: temp.append(root.left.val)
        if root.right: temp.append(root.right.val)
        elif not root.left: return

        stack.append([])
        stack[i] = stack[i] + temp

        bfs(root.left, i+1)
        bfs(root.right, i+1)

    bfs(root, 1)

    return [arr for arr in stack[::-1] if len(arr) > 0]



root = CreateTree([3,9,20,None,None,15,7])
PrintTree(root)
bcolors.Test(levelOrderBottom(root), [[15,7],[9,20],[3]])


root = CreateTree([1])
PrintTree(root)
bcolors.Test(levelOrderBottom(root), [[1]])


root = CreateTree([])
PrintTree(root)
bcolors.Test(levelOrderBottom(root), [])


root = CreateTree([1,2,3,4,None,None,5])
PrintTree(root)
bcolors.Test(levelOrderBottom(root), [[4,5],[2,3],[1]])