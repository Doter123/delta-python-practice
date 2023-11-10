import sys
sys.path.append('../PrintTree')
from PrintTree import PrintTree
sys.path.append('../CreateBinaryTree')
from CreateBinaryTree import CreateTree, TreeNode

from typing import Optional, List
from collections import deque 

def binaryTreePaths(root: Optional[TreeNode]):

    result_pipe = []

    def getTreePipes(root, pipe):
        if not root: return

        pipe = pipe.copy()

        pipe.append(str(root.val))

        if root.left:
            getTreePipes(root.left, pipe)
        if root.right:
            getTreePipes(root.right, pipe)
        if not root.right and not root.left:
            result_pipe.append("->".join(pipe))

    getTreePipes(root, [])

    return result_pipe

levels = [1,2,3,None,5]
tree = CreateTree(levels)
PrintTree(tree)

print(binaryTreePaths(tree)) # ['1->2->5', '1->3']

levels = [1,2,3,None,5, 7, 1]
tree = CreateTree(levels)
PrintTree(tree)

print(binaryTreePaths(tree)) # ['1->2->5', '1->3->7', '1->3->1']