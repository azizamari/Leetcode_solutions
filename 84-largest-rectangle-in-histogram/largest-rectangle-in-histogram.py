class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        maxi=0
        for i in range(len(heights)):
            h=heights[i]
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxi = max(maxi, height * (i - index))
                start = index
            stack.append((start, h))
        for i, h in stack:
            maxi = max(maxi, h * (len(heights) - i))
        return maxi
