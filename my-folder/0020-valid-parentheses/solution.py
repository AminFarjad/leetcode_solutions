class Solution:
    def isValid(self, s: str) -> bool:
        arr = []
        if len(s)%2 !=0:
            return False
        str1=s
        for s in str1:
            if s in ['}',']',')']:
                if len(arr)==0:
                    return False
                removed = arr.pop()
                if s== '}' and removed != '{':
                    return False
                if s==')' and removed != '(':
                    return False
                if s==']'  and removed != '[':
                    return False
            elif s in ['{','[','(']:
                arr.append(s)
        if len(arr)!=0:
            return False
        return True



        
