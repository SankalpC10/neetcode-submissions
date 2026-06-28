class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = sorted(list(set(nums)))
        print(numset)
        if len(numset) == 0:
            return 0
        max_seq = 1
        temp = 1
        for i in range(1,len(numset)):
            if numset[i]-numset[i-1] == 1:
                temp += 1
                max_seq = max(temp,max_seq)
            else:
                temp = 1
        return max_seq

