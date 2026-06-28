class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        num_zeros,l,r=0,0,0
        while r<len(nums):
            if nums[r]!=0:
                nums[l]=nums[r]
                l+=1
            else:
                num_zeros+=1
            r+=1
        for i in range(l,(len(nums))):
            nums[i]=0

                


        