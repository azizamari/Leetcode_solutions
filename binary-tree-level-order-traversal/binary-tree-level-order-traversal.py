# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]
        res_f=[]
        def printLevel(root,level):
            if root==None:return
            if level>0:
                printLevel(root.left,level-1)
                printLevel(root.right,level-1)
            else:
                res.append(root.val)
        def height(root):
            if root==None:return 0
            return 1 + max(height(root.left),height(root.right))
        for i in range(height(root)):
            printLevel(root,i)
            res_f.append(res)
            res=[]
        return res_f