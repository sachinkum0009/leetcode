"""
Given the root of a binary tree, split the binary tree into two subtrees by removing one edge such that the product of the sums of the subtrees is maximized.

Return the maximum product of the sums of the two subtrees. Since the answer may be too large, return it modulo 109 + 7.

Note that you need to maximize the answer before taking the mod and not after taking it.
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
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        all_sums = []

        def sum_tree(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0

            s = node.val + sum_tree(node.left) + sum_tree(node.right)

            all_sums.append(s)
            return s

        total_sum = sum_tree(root)
        best = 0

        for s in all_sums:
            best = max(best, s * (total_sum - s))

        return best % (10**9 + 7)


def make_tree(root: List[int]) -> TreeNode | None:
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
    root = [1, 2, 3, 4, 5, 6]
    tree = make_tree(root)
    result = Solution().maxProduct(tree)
    print(f"result: {result}")


if __name__ == "__main__":
    main()
