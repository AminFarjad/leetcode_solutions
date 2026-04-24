class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) == 2:
            return 1 * min(height[0],height[1])
        i = 0 
        j = len(height) - 1
        area = 0
        le = len(height) - 1
        while i < j:
            temp = min(height[i],height[j]) * le
            if temp> area:
                area = temp
            if height[i]<height[j]:
                i += 1
            elif height[i] > height[j]:
                j-=1
            else:
                i+=1
                j-=1
                le-=1
            le -=1
        return area


        # maxi = max(height)
        # index = height.index(maxi)
        # i = 0 
        # l = len(height)
        # area = 0
        # while i < l:
        #     if i == index:
        #         i+=1
        #         continue
        #     aaa = min(height[i],maxi) * abs(index - i)
        #     if aaa> area:
        #         area= aaa
        #     i+=1
        # return area
        
        # i = 2
        
        # a = height[0]
        # b = height[1]
        # area2 = min(a,b)
        # diff = 1
        # h = len(height)
        # an = 1
        # while i < h:
        #     c = min(a,height[i]) * (diff + 1)
        #     d = min(b,height[i]) * (an)
        #     if c > d and c > area2:
        #         a = a
        #         b = height[i]
        #         area2 = c
        #         diff+=1
        #         an = 1
        #     elif d > area2:
        #         a = b
        #         b = height[i]
        #         area2 = d
        #         diff=1
        #         an = 1
        #     else:
        #         diff+=1
        #         an +=1
        #     i+=1
        # print(a,b)
        # return max(area,area2)
            





        
