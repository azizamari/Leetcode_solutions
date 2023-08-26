class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        denom = sum(self.w)
        for i in range(len(self.w)):
            self.w[i] = self.w[i] / denom
        for i in range(1,len(self.w)):
            self.w[i] += self.w[i-1]
        print(self.w)

    def pickIndex(self) -> int:
        n=random.uniform(0,1)
        i=0
        while i<len(self.w):
            if n<=self.w[i]:
                return i
            i+=1
        return i       

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()