class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(i, s):
            if i == len(nums):
                res.append(s.copy())
                return

            s.append(nums[i])
            backtrack(i + 1, s)

            s.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1, s)

        backtrack(0, [])
        return res
