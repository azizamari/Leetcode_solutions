class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        cnter = defaultdict(int)
        res = 0
        for t in time:
            t %= 60
            res += cnter[(60-t) % 60]
            cnter[t] += 1
            
        return res