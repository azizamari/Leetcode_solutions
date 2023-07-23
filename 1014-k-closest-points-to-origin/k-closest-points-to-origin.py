import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pts = []
        heapq.heapify(pts)
        for x, y in points:
            dist = (abs(x - 0) ** 2) + (abs(y - 0) ** 2)
            heapq.heappush(pts,[dist, x, y])
        return [[x[1],x[2]] for x in heapq.nsmallest(k, pts)]