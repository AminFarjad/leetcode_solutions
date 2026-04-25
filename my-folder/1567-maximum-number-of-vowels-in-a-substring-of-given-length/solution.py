class Solution:
    def countvowels(self,stri):
        count = 0
        for s in stri:
            if s in ['a','e','i','o','u']:
                count +=1
        return count
    def maxVowels(self, s: str, k: int) -> int:
        if k >=len(s):
            return self.countvowels(s)
        
        
        sub_str = s[0:k]
        sub_count = self.countvowels(sub_str)
        max_sub_count = sub_count
        first_vowel = self.countvowels(s[0])
        i = k
        while i < len(s):
            sub_count -= first_vowel
            if s[i] in ['a','e','i','o','u']:
                sub_count +=1
            i+=1
            first_vowel = self.countvowels(s[i-k])
            if sub_count > max_sub_count:
                max_sub_count = sub_count
        
        return max_sub_count
            


        




        
