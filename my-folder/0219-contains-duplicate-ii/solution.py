class Solution:

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        nums_dic =  {}
        le = len(nums)
        i = 0
        while i <= k and i < le:
            if nums[i] in nums_dic:
                nums_dic[nums[i]].append(i)
                if abs(nums_dic[nums[i]][-1] - i) <=k:
                    return True
            else:
                nums_dic[nums[i]] = [i]
            # print(nums_dic)
            i+=1
        
        
        
        while i < le:
            if nums[i] in nums_dic:
                
                if nums_dic[nums[i]] and abs(nums_dic[nums[i]][-1]-i) <=k:
                    return True
                nums_dic[nums[i]].append(i)
            else:
                nums_dic[nums[i]]=[i]
            temp = nums[i-k]
            if temp in nums_dic:
                nums_dic[temp].pop(0)
            # print(nums_dic)
            i+=1
        
        return False
            
            

