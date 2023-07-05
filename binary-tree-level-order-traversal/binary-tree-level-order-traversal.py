# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]
        def printLevel(root,level):
            if root==None:return
            if len(res)<level+1:
                res.append([root.val])
            else: 
                res[level].append(root.val)
            printLevel(root.left,level+1)
            printLevel(root.right,level+1)
        printLevel(root,0)
        return res