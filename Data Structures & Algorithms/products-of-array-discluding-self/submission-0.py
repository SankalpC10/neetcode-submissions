class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_arr = [1]*len(nums)
        running_product = nums[0]
        for i in range(1,len(nums)):
            product_arr[i] *= running_product
            running_product *= nums[i]
        running_product = nums[-1]
        for i in range(len(nums)-2,-1,-1):
            product_arr[i] *= running_product
            running_product *=nums[i]
        return product_arr