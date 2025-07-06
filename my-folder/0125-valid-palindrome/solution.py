class Solution:
    def isPalindrome(self, s: str) -> bool:
        st=s.lower()
        temp = ""
        for s in st:
            if s in list("abcdefghijklmnopqrstuvwxyz0123456789"):
                temp+=s
        return temp == temp[::-1]
        
