class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num]+=1
        l = list(count.keys())
        print(count)
        sum = 0
        for li in l:
            if li >= k:
                continue
            temp = abs(k-li)
            if temp in count and count[temp]!=0 and temp != li and count[li]!=0:
                count[temp]-=1
                sum +=1
                count[li]-=1
                while count[temp]>0 and count[li]>0:
                    sum+=1
                    count[li]-=1
                    count[temp]-=1
            elif temp == li and count[temp]>1:
                tee= count[temp]//2
                count[temp]-=(tee*2)
                sum+=tee
        return sum
                

        
