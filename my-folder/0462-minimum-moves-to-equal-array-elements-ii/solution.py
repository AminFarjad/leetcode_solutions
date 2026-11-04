class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        mid = len(nums)
        mid = mid - (1 - mid%2)
        mid = nums[mid//2]
        temp = 0
        for num in nums:
            temp += abs(num-mid)
        return temp

