class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = {}
        t_count = {}
        if len(s) == len(t):
            for i in range(len(s)):
                if s[i] in s_count: s_count[s[i]] +=1
                else: s_count[s[i]] = 1
                if t[i] in t_count: t_count[t[i]] +=1
                else: t_count[t[i]] = 1
            if (s_count == t_count): return True
            else: return False
        else: return False 
