class Solution:
    def minDeletions(self, nums: list[int]) -> int:

        temp = [nums[0]]

        i=1
        l = len(nums)
        while i < l:
            if temp[-1] ^ nums[i] !=0:
                temp.append(nums[i])
            i+=1

        return l - len(temp)
            
        
