class Solution:
    def isValid(self, s: str) -> bool:
        arr = []
        complementary_dict = {')':'(',']':'[','}':'{'}
        for i in s:
            if i in complementary_dict and len(arr) != 0:
                if arr[-1] != complementary_dict[i]:
                    return False
                else:
                    arr.pop()
            else:
                arr.append(i)
        return len(arr)==0