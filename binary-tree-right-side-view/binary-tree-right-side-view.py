# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode | None) -> List[int]:
        # basically level order traversal but print only rightmost node
        if not root:
            return []
        ans = []        
        q = [root]
        while q:            
            ans.append(q[-1].val)
            q = [child for node in q for child in (node.left, node.right) if child]

        return ans
