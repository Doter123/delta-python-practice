

# Definition for a binary tree node.
from collections import deque
from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def CreateTree(levels: List[int]) -> Optional[TreeNode]:
    if len(levels) == 0:
        return None

    i = 1
    root = TreeNode(levels[0])
    queue = deque([root])

    while queue and i < len(levels):
        node = queue.popleft()

        if i < len(levels):
            if levels[i] != None:
                node.left = TreeNode(levels[i])
                queue.append(node.left)
            i += 1

        if i < len(levels):
            if levels[i] != None:
                node.right = TreeNode(levels[i])
                queue.append(node.right)
            i += 1

    return root

# nodes = [1, 2, 3, 4, 5]

# root = TreeNode(nodes[0])
# root.left = TreeNode(nodes[1])
# root.right = TreeNode(nodes[2])
# root.left.left = TreeNode(nodes[3])
# root.left.right = TreeNode(nodes[4])
