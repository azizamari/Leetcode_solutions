from queue import PriorityQueue
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        q=PriorityQueue()
        [q.put(-x) for x in stones]
        while True:
            n=q.qsize()
            if n==1:
                return -q.get()
            elif n==0:
                return 0
            else:
                x=-q.get()
                y=-q.get()
                if x!=y:
                    q.put(-abs(x-y))
        