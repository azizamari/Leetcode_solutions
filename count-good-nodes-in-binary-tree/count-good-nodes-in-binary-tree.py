# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def get(root, maxim):
            if root==None:
                return 0
            elif root.val>=maxim:
                return 1+get(root.left,root.val)+get(root.right,root.val)
            else: return get(root.left,maxim)+get(root.right,maxim)
        return get(root,root.val)