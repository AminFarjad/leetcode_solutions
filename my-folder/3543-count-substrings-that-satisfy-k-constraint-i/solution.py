class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        count_dic = {}
        i = 0
        sum = 0
        size = 0
        for letter in s:
            if letter in count_dic:
                count_dic[letter]+=1
            else:
                count_dic[letter] = 1
            size += 1
            while count_dic.get('0',0) > k and count_dic.get('1',0) > k:
                count_dic[s[i]]-=1
                sum += size - 1
                i+=1
                size -=1
        
        return int(sum + ((size *(size+1))/2))





        
