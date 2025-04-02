class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # ABABAB     ABCABC      ABCDABCD    
        if str1+ str2 != str2+str1:
            return ""
        else:
            return str1[:math.gcd(len(str1),len(str2))]
        
