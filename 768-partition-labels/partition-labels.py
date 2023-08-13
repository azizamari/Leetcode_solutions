class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # first , last
        pos=OrderedDict()
        for i, val in enumerate(s):
            if not val in pos:
                pos[val]=[i,0]
            pos[val][1]=i
        print(pos)
        start=0
        res=[]
        poss=list(pos.values())
        while start<len(s):
            end=pos[s[start]][1]
            i=0
            while i<len(pos):
                if poss[i][0]>end:
                    break
                elif poss[i][0]<end and poss[i][0] >start:
                    end=max(poss[i][1],end)
                i+=1
            res.append(end-start+1)
            start=end+1
        return res