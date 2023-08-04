class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]: 
        res = []
        intervals=sorted(intervals,key=lambda x: x[0])
        i=0
        while i < len(intervals)-1:
            if intervals[i][1] < intervals[i+1][0]:
                res.append(intervals[i])
            else:
                intervals[i+1][0]=min(intervals[i][0],intervals[i+1][0])
                intervals[i+1][1]=max(intervals[i+1][1], intervals[i][1])
            i+=1
        res.append(intervals[-1])
        return res

            
