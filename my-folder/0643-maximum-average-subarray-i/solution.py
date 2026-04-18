class Solution:
    def find_sum(self, nums):
        sum = 0
        for num in nums:
            sum += num
        return sum
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        le = len(nums)
        if le == k:
            return self.find_sum(nums)/k

        sum = self.find_sum(nums[0:k])
        avg = sum/k
        i = k
        while i < le:
            sum+=nums[i]
            sum-=nums[i-k]
            temp = sum/k
            if temp > avg:
                avg = temp
            i+=1
        return avg
            

    
        
