class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        i=0
        j=0
        l=0
        while l < len(haystack):
            if i==len(needle):
                return j
            if needle[i]==haystack[l]:
                if i==0:
                    j=l
                i+=1
            elif i!=0:
                i=0
                l=j
                j=0
                
            l+=1

        return j
            
        
