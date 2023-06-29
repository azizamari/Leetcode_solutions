class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[]

        for i, t in enumerate(temperatures[:-1]):
            res.append(0)
            if t< temperatures[i+1]:
                j=i
                while j>=0 and temperatures[j]<temperatures[i+1]:
                    if res[j]==0:
                        res[j]=i+1-j
                    j-=1
        return res+[0]