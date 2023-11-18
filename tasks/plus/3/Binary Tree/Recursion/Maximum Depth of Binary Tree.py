import sys
sys.path.append('../PrintTree')
sys.path.append('../CreateBinaryTree')
from PrintTree import PrintTree
from CreateBinaryTree import CreateTree, TreeNode
from typing import Optional


def maxDepth(root: Optional[TreeNode]) -> int:
    def dfs(node, depth):
        return depth if not node else max(dfs(node.left, depth+1), dfs(node.right, depth+1))
    return dfs(root, 0)



root = CreateTree([3,9,20,None,None,15,7])

PrintTree(root)
print(maxDepth(root)) # 3



root = CreateTree([1,None,2])

PrintTree(root)
print(maxDepth(root)) # 2