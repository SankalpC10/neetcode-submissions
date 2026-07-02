class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        hashmap = {}
        max_chain = 1
        for num in nums:
            if num-1 in hashmap:
                max_chain = max(max_chain,1+hashmap[num-1])
                hashmap[num] = 1+hashmap[num-1]
            else:
                hashmap[num] = 1
        return max_chain