class Solution:
    def verify(self, dic, nums):
        s = set()
        i=1
        for num in nums:
            if num not in s:
                s.add(num)
                if dic[num]!=i:
                    return False
                i+=1
        return True
                
    def countStaircase(self, nums: list[int]) -> int:
        su = len(nums)
        i = 0
        t = 0
        while i < su:
            dic = {nums[i]:1}
            # print(dic)
            j = i+1
            le = 1
            dic_len=1
            while j < su:
                if nums[j] in dic:
                    dic[nums[j]]+=1
                else:
                    dic[nums[j]]=1
                    dic_len+=1
                le +=1
                # print(le,dic_len)
                if le == (dic_len * (dic_len+1))/2 and le!=1:
                    # print(dic)
                    # print(nums[i:j+1])
                    ans = self.verify(dic,nums[i:j+1])
                    # print(ans)
                    if ans == True:
                        t+=1


                j+=1
            i+=1
        return su+t
        
