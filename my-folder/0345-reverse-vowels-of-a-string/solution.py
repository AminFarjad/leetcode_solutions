class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels=['a','e','i','o','u','A','E','I','O','U']
        newli=[]
        for word in s:
            if word in vowels:
                newli.append(word)

        newstr=''
        for word in s:
            if word in vowels:
                newstr+=newli.pop()
            else:
                newstr+=word
        return newstr
