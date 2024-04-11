class Solution:
    def an(self, s):
        i = 0
        char = s[0]
        n = len(s)
        while i < n:
            char = s[i]
            j = i+1
            while j < n:
                if char == s[j]:
                    n = j
                    break
                j += 1
            i += 1
        return len(s[0:i])

    def lengthOfLongestSubstring(self, s: str) -> int:
        temp = 0
        for i in range(0,len(s)):
            temp = max(temp,self.an(s[i:]))
        return temp
