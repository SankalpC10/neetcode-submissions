class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs[0])):
            cur = strs[0][:i+1]
            for j in strs:
                if j.startswith(cur):
                    continue
                else:
                    return res
            res = cur
        return res
                    
