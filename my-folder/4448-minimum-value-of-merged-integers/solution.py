class Solution:
    def minMergedInteger(self, nums: list[int]) -> int:
        temp = []
        while nums:
            first = nums.pop(0)
            second = nums.pop(0)
            num = str(first) + str(second)
            temp.append(int(num))
        return min(temp)
            
        
        
