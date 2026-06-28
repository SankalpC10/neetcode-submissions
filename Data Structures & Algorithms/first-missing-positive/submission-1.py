class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(1,max(nums)):
            if i not in nums:
                return i
        return max(max(nums)+1,1)