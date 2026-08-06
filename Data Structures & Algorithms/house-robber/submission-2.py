class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        n = len(nums)
        def max_rob(i):
            if i < 0:
                return 0
            if i == 0:
                return nums[0]
            
            if i in memo:
                return memo[i]
            skip = max_rob(i-1)
            not_skip = max_rob(i-2)+nums[i]
            memo[i] = max(skip,not_skip)
            return memo[i]
        return max_rob(n - 1)