import sys
sys.path.append('../PrintTree')
sys.path.append('../CreateBinaryTree')
from PrintTree import PrintTree, bcolors
from CreateBinaryTree import CreateTree, TreeNode
from typing import Optional, List
from collections import Counter

def findMode(root: Optional[TreeNode]) -> List[int]:
    def bfs(root):
        if not root: return []
        return [root.val] + bfs(root.left) + bfs(root.right)
    cnt = Counter(bfs(root))
    maxx = max(cnt.values())

    return [val for val, count in cnt.items() if count == maxx]


root = CreateTree([1,None,2,2])
PrintTree(root)
bcolors.Test(findMode(root), [2])


root = CreateTree([0])
PrintTree(root)
bcolors.Test(findMode(root), [0])