class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=len(nums)
        k=k-1
        z=k+1
        while k > 0 :
            if nums[k]==nums[k-1]:
                nums.pop(k)
            k=k-1
        

