class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = []
        for ch in operations:
            if ch == "C":
                score.pop()
            elif ch == "D":
                score.append(score[-1]*2)
            elif ch == "+":
                score.append(score[-1]+score[-2])
            else:
                score.append(int(ch))
        return sum(score)