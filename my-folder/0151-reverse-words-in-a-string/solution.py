class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.rstrip()
        li = s.split(' ')

        newstr=''
        while li:
            new = li.pop().rstrip()
            newstr+=new
            newstr+=' ' if len(new)>0 else ''
        
        return newstr[:-1]
