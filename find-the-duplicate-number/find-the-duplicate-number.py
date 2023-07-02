class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        length = len(nums)
        low = 1
        high = length - 1

        while low < high:
            mid = (low + high) // 2
            count = 0

            for i in range(length):
                if nums[i] <= mid:
                    count += 1

            if count <= mid:
                low = mid + 1
            else:
                high = mid
        return low