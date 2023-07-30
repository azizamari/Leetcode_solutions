class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits=='': return []
        mapping={}
        c=97
        for i in  range(2,10):
            jump=3
            if i==7 or i==9:
                jump+=1
            mapping[i]=''.join([chr(c+x) for x in range(jump)])
            c+=jump
        res=[]
        def dfs(word,i):
            if i==len(digits): 
                res.append(word)
                return 
            for c in mapping[int(digits[i])]:
                dfs(word+c,i+1)
        dfs('',0)
        return res
