# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.last=float('-inf')
        def validate(root):
            if not root: return True
            v=validate(root.left)
            if root.val>self.last: 
                self.last=root.val
            else: return False
            w=validate(root.right)
            return v and w
        return validate(root)