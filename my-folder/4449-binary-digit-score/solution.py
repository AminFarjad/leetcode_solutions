class Solution:
    def calculateScore(self, a: int, b: int) -> int:
        a = bin(a)
        s1 = 0
        for s in a:
            if s == '1':
                s1+=1
        b=bin(b)
        s2 = 0
        for s in b:
            if s == '1':
                s2+=1

        if s1>=s2:
            return s1*s2
        else:
            return s2//s1
