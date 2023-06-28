class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for num in nums:
            if not num in count: count[num]=0
            count[num]+=1
        return sorted(count, key=count.get, reverse=True)[:k]
