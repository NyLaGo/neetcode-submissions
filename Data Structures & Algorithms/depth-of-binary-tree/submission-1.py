# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        depth = 0
        queue = [root]

        while queue:
            n = len(queue)

            for i in range(n):
                removed = queue.pop(0)

                if removed.left:
                    queue.append(removed.left)
                if removed.right:
                    queue.append(removed.right)

            depth += 1

        return depth