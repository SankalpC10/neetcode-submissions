class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        req = [i for i in nums if i!=val]
        nums[:len(req)] = req
        return len(req)