class Solution:
    def switch(self, num):
        digit_list = [int(x) for x in str(num)]

        le = len(digit_list)
        digit_list.sort(reverse=True)
        # print(digit_list)
        i=0
        # while i < le//2:
        #     if digit_list[i] < digit_list[le - i - 1]:
        #         temp = digit_list[i]
        #         digit_list[i] = digit_list[le - i - 1]
        #         digit_list[le - i - 1] = temp
        #     i += 1

        st = ''
        for i in digit_list:
            st += str(i)
        return int(st)
            
    def maximizeSum(self, nums: list[int], k: int) -> int:
        rearranged = []
        mi = 0
        su = 0
        for num in nums:
            temp_num = self.switch(num)
            rearranged.append(temp_num - num)
        rearranged.sort(reverse=True)
        su = sum(nums)
        # print(su)
        print(rearranged)
        for num in rearranged:
            if num <= 0:
                break
            if k !=0:
                su += num
                k-=1
        return su
        
            
