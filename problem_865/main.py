from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return 0, None
            
            left_depth, left_node = dfs(node.left)
            right_depth, right_node = dfs(node.right)
            
            if left_depth > right_depth:
                return left_depth + 1, left_node
            
            elif right_depth > left_depth:
                return right_depth + 1, right_node
            
            else:
                return left_depth + 1, node

        return dfs(root)[1]

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
    root = [3,5,1,6,2,0,8,None,None,7,4]
    tree = make_tree(root)
    result = Solution().subtreeWithAllDeepest(tree)
    print(f"result: {result.val}, {result.left.val}, {result.right.val}")

if __name__ == '__main__':
    main()
