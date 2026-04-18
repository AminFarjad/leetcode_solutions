class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum = 0
        for num in nums:
            sum +=num
        left_sum = 0
        i=0
        for num in nums:
            
            temp = sum - num
            tt= temp/(2.0)
            if left_sum == tt:
                return i
            left_sum +=num
            i+=1

        return -1
        # i = 0
        # j = len(nums) - 1
        # right_sum = nums[-1]
        # left_sum = nums[0]
        # if len(nums)==2 and right_sum +left_sum ==0:
        #     return 0

        # while i < j:
        #     if left_sum < right_sum:
        #         i+=1
        #         left_sum += nums[i]
        #     elif right_sum < left_sum:
        #         j-=1
        #         right_sum += nums[j]
        #     else:
        #         i+=1
        #         j-=1
        #         left_sum +=nums[i]
        #         right_sum +=nums[j]

        # if right_sum == left_sum and i==j:
        #     return i
        # if i == 0 and right_sum == 0:
        #     return i
        # elif j == len(nums)-1 and left_sum ==0:
        #     return j
        # return -1
        
