class Solution:
    

    def minWindow(self, s: str, t: str) -> str:
        if len(s) == len(t) and s == t:
            return s
        elif len(s) < len(t):
            return ""
        elif len(t) ==1 and t in s:
            return t
        
        dic = {}
        for tt in t:
            num = s.find(tt)
            prev_num = 0
            while num in dic :
                prev_num = num
                num = s[num+1:].find(tt) + 1
                if num == 0:
                    return ""
                num += prev_num
            if num == "-1":
                return ""
            dic[num] = tt
        print(dic)


    #         prev_num = 0
    # while num in dic :
    #     prev_num = num
    #     num = s[num+1:].find(tt) + 1
    #     if num == 0:
    #         print("afdaf")
    #         break
    #     num += prev_num
    # dic[num+prev_num] = tt


    # num = s.find(tt)
    # prev_num = 0
    # while num in dic :
    #     print(tt,num)
    #     prev_num = num
    #     print(s[num+1:])
    #     num = s[num+1:].find(tt) + 1
    #     if num == 0:
    #         print("afdaf")
    #     num += prev_num
    # dic[num] = tt

        k = max(list(dic.keys()))
        t = min(list(dic.keys()))
        substr = s[t:k+1]

        mini = min(list(dic.keys()))
        char_to_find = dic.pop(mini)
        last_value = mini
        i = mini +1
        
        while i < len(s):
            if s[i] == char_to_find:
                if i in dic:
                    i+=1
                    continue
                dic[i] = s[i]
                mini = min(list(dic.keys()))
                maxi = max(list(dic.keys()))
                char_to_find= dic.pop(mini)
                up = min(mini,i)
                temp_sub = s[up:maxi+1]
                if len(temp_sub) < len(substr):
                    substr=temp_sub
            elif s[i] in dic.values():
                key = next(k for k, v in dic.items() if v == s[i])
                dic.pop(key)
                dic[i] = s[i]
            i+=1



        return substr
            

            
            





            
        



    

