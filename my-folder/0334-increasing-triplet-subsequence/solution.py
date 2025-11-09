class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        a = sys.maxsize
        b = sys.maxsize

        for num in nums:
            if a>=num:
                a= num
            elif b>=num:
                b=num
            else:
                return True
        
        return False
        
