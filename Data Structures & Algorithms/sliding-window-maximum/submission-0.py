class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        L = 0
        for R in range(k,len(nums)+1):
            req = nums[L:R]
            curr_max = max(req)
            res.append(curr_max)
            L += 1
        return res