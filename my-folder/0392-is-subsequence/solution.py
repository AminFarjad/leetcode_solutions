class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        length = len(s)
        if len(s)<1:
            return True
        i=0
        for val in t:
            if s[i]==val:
                i+=1
            if i == length:
                return True
        
        return False
