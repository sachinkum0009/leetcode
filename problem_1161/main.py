"""
Problem: 1161
Maxium Level Sum of a Binary Tree

Given the `root` of a binary tree, the level of its root is 1, the level of its childern is 2, and so on.
Return the *smallest* level `x` such that the sum of all the values of dones at level x is maximal.
"""

from typing import Optional, List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = deque([root])
        max_sum = root.val
        max_level = 1
        current_level = 1
        while queue:
            level_sum = 0
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.popleft()
                level_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if level_sum > max_sum:
                max_sum = level_sum
                max_level = current_level
            current_level += 1
        return max_level


def make_tree(root: List[int]) -> TreeNode:
    if not root or root[0] is None:
        return None
    nodes = []
    for val in root:
        node = TreeNode(val) if val is not None else None
        nodes.append(node)
    kids = nodes[::-1]
    root_node = kids.pop()
    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()
    return root_node


def main():
    root = [1, 7, 0, 7, None, None]
    tree = make_tree(root)
    result = Solution().maxLevelSum(tree)
    print(f"result is {result}")


if __name__ == "__main__":
    main()
