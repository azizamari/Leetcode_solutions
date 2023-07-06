# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k=k
        self.res=-1
        def inorder(root):
            if not root: return 
            inorder(root.left)
            if self.k==1:
                self.k-=1
                self.res=root.val
                return 
            self.k-=1
            inorder(root.right)
        inorder(root)
        return self.res