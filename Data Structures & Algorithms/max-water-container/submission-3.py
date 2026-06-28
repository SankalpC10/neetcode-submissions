class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights)-1
        max_area = 0
        while(i<j):
            output = (min(heights[i] ,heights[j])) * (j-i)
            if output > max_area:
                max_area = output
            if heights[i]>=heights[j]:
                j -= 1
            if heights[j]>heights[i]:
                i += 1
        return max_area