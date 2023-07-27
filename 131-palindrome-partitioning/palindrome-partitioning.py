class Solution:
    def partition(self, s: str) -> List[List[str]]:
        output=[]          
        def dfs(i,sub):
            if i>=len(s): 
                output.append(sub.copy())
                return 
            for j in range(i,len(s)):
                if s[i:j+1]==s[i:j+1][::-1]:
                    dfs(j+1, sub+[s[i:j+1]])
        dfs(0,[])
        return output