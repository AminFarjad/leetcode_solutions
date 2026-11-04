class Solution:
    def minMoves(self, nums: list[int]) -> int:
        max_num = max(nums)
        max_sum = 0
        for num in nums:
            max_sum += abs(num-max_num)
        return max_sum


    
        
