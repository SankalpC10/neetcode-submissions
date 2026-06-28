class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter = {}
        for i in nums:
            if i in counter.keys(): counter[i] += 1
            else: counter[i] = 1
        for j in counter.values():
            if j>1: return True
        
        return False
        