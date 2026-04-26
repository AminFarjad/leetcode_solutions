class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        max_count = 0
        i = 0 
        l = len(nums)
        temp = 0
        started = 0
        even = 0
        while i < l:
            if not started and nums[i] % 2 == 0 and nums[i] <= threshold:
                started = 1
                temp +=1
                even = 0
            elif started and even and nums[i]%2==0 and nums[i] <= threshold:
                temp +=1
                even = 0
            elif started and not even and nums[i]%2!=0 and nums[i]<=threshold:
                temp +=1
                even = 1
            elif nums[i] > threshold and started:
                if temp > max_count:
                    max_count = temp
                temp = 0
                started = 0
            elif started:
                if temp > max_count:
                    max_count = temp
                temp = 0
                started = 0
                i -= (1-nums[i]%2) 

            i+=1
        return max(max_count,temp)
            
            


