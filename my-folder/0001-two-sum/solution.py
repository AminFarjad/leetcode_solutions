class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic={}
        z=0
        for i in nums:
            dic[i]=z
            z+=1
        
        for i in range(0,len(nums)):
            if target-nums[i] in dic and i!=dic[target-nums[i]]:
                return [i,dic[target-nums[i]]]
         
        
        
