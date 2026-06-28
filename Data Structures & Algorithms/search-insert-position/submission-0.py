class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        L,R = 0, len(nums)
        while L<R:
            M = L+(R-L)//2
            if nums[M] >=target:
                R = M
            elif nums[M]<target:
                L = M+1
        return L
