class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        
        i = 0
        for num in nums:
            nums[i]=abs(num)
            i+=1
        print(nums)

        nums.sort()
        sum =0
        i=0
        l=len(nums)
        for num in nums:
            if i < l//2:
                sum -= (num*num)
            else:
                sum += (num*num)
            i+=1
        return sum
