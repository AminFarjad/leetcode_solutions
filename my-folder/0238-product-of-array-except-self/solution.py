class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        product = nums[0]
        temp = []
        count = 0
        zeros=0
        for val in nums:
            if val!=0:
                count+=1
            else:
                zeros+=1
        if all(x == 0 for x in nums) or (count ==1 and len(nums)!=2) or zeros>1:
            return [0]*len(nums)

        
        if 0 in nums:

            product = 1
            for val in nums:
                if val != 0:
                    product *= val
             
            for val in nums:
                if val !=0:
                    temp.append(0)
                else:
                    temp.append(product)

        else:
            for val in nums:
                product *= val
            product = product//nums[0]
            
            for val in nums:
                temp.append(product//val)

        return temp
        
