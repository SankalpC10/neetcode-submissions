class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = x
        neg = False
        if n<0:
            neg = True
        if n==0:
            return 1
        n = abs(n)
        for _ in range(1,n):
            res*=x
        return 1/res if neg else res