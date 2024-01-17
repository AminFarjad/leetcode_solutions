class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict={}
        for num in nums:
            if num not in dict:
                dict[num]=1
            else:
                dict[num]+=1
        max = nums[0]
        for key in dict.keys():
            if dict[max] < dict[key]:
                max = key
        return max
