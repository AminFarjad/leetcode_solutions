class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = len(word1)
        j = len(word2)

        temp = ""
        k = 0
        m = 0
        while k < i and m < j:
            temp += word1[k]
            k+=1
            temp += word2[m]
            m+=1
        
        while k < i:
            temp +=word1[k]
            k+=1
        while m < j:
            temp += word2[m]
            m+=1
        
        return temp



