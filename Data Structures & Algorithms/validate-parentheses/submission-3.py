class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = { "}":"{", "]":"[", ")":"("}
        stack = []
        for ch in s:
            if ch in hashmap:
                if not stack:
                    return False
                elif stack[-1] != hashmap[ch]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(ch)
        return len(stack)==0