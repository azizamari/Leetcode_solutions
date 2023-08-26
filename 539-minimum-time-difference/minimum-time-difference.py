class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def convert(time):
            h=int(time[:2])
            m=int(time[3:])
            return h*60 + m
        timePoints=[convert(t) for t in timePoints]
        res=float(inf)
        timePoints.sort()
        print(timePoints)
        for i in range(len(timePoints)-1):
            res=min(res, timePoints[i+1]-timePoints[i])
        res=min(res, -timePoints[-1]+timePoints[0]+1440)
        return res
