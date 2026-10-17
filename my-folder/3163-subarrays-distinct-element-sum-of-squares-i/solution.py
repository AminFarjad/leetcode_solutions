class Solution:
    def cnt(self,temp):
        dic = {}
        for num in temp:
            if num not in dic:
                dic[num]=1
            else:
                dic[num]+=1
        return dic


    def sumCounts(self, nums: List[int]) -> int:

        dic = {}
        i = 1
        le = len(nums)
        count = le
        while i < le:
            temp = deque(nums[0:i+1]) 
            dic = self.cnt(temp)
            dic_len= len(dic.keys())
            count += (dic_len*dic_len)
            k=0
            while k < le - (i+1):
                
                first = temp.popleft()
                
                dic[first]-=1
                if dic[first]==0:
                    del dic[first]
                    dic_len -=1
                t = nums[i+k+1]
                temp.append(t)
                if t not in dic:
                    dic[t]=1
                    dic_len+=1
                elif t in dic:
                    dic[t]+=1
                count += (dic_len*dic_len)
                k+=1
            i+=1
        return count % (pow(10,9)+7)


