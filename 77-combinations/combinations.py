class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]
        def dfs(i,k, curr):
            if k==0:
                res.append(curr)
                return
            if i>n: return
            dfs(i+1,k-1,curr+[i])
            dfs(i+1,k,curr)
        dfs(1,k,[])
        return res