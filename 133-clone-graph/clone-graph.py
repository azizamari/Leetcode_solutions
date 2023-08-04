"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return None
        self.nodes={}
        def helper_vals(neighbors):
            res=[]
            for n in neighbors:
                res.append(n.val)
            return res
        def helper_nodes(neighbors):
            res=[]
            for n in neighbors:
                res.append(self.nodes[n])
            return res
        def dfs(n):
            if not n or n.val in self.nodes:
                return 
            else:
                self.nodes[n.val]=Node(n.val,helper_vals(n.neighbors))
                for no in n.neighbors:
                    dfs(no)
        dfs(node)
        for x in self.nodes.values():
            x.neighbors=helper_nodes(x.neighbors)
        return self.nodes[node.val]
