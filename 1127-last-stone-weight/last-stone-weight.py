from queue import PriorityQueue
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        q=PriorityQueue()
        [q.put(-x) for x in stones]
        n=len(stones)
        while True:            
            if n==1:
                return -q.get()
            elif n==0:
                return 0
            else:
                x=-q.get()
                y=-q.get()
                n-=2
                if x!=y:
                    n+=1
                    q.put(-abs(x-y))
        