class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        res = [len(heights)-1]
        max_right = heights[-1]
        for i in range(len(heights)-1,-1,-1):
            if heights[i]>max_right:
                max_right = heights[i]
                res.append(i)
        return res[::-1]
