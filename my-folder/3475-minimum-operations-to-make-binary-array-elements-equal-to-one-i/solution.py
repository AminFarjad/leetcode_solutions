class Solution:
    def minOperations(self, nums: List[int]) -> int:

        i = 0
        count = 0
        le = len(nums)
        while i < le - 3:
            if nums[i] == 0:
                nums[i] = 1 - nums[i]
                nums[i+1] = 1 - nums[i+1]
                nums[i+2] = 1 - nums[i+2]
                count +=1
            i+=1
        
        
        if nums[-1] == nums[-2] and nums[-2]==nums[-3]:
            return count + (1-nums[-1])
        else:
            return -1
        
