class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l=len(nums)
        self.i=1
        r=1
        prev=nums[0]
        count = 0
        while self.i < l:
            if nums[self.i]==prev:
                count+=1
            else:
                count =0 
                prev = nums[self.i]
            
            if count == 2:
                while self.i<l and nums[self.i]==prev:
                    self.i+=1
                count = 0
                if self.i < l:
                    prev=nums[self.i]
            if self.i<l:
                nums[r]=nums[self.i]
                print(r,self.i)
                r+=1
                self.i+=1

        return r
                

