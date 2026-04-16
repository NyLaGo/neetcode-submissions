# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(root, subRoot):
            if not root and not subRoot:
                return True
            if not root or not subRoot:
                return False
            if root.val != subRoot.val:
                return False
            
            return isSameTree(root.left, subRoot.left) and isSameTree(root.right, subRoot.right)

        queue = [root]
        result = False

        while queue:
            n = len(queue)

            for i in range(n):
                removed = queue.pop(0)
                
                if removed.left:
                    queue.append(removed.left)
                if removed.right:
                    queue.append(removed.right)
                
                if removed.val == subRoot.val:
                    dummy = subRoot
                    result = isSameTree(removed, dummy)

                    if result:
                        return True

        return False


