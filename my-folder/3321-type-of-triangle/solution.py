class Solution:
    def triangleType(self, nums: List[int]) -> str:
        a = nums[0]
        b = nums[1]
        c = nums[2]
        if a==b and b==c and a!=0:
            return 'equilateral'
        
        elif a+b>c and b+c>a and a+c>b:
            if (a==b) or (a==c) or (b==c):
                return 'isosceles'
            else:
                return 'scalene'
        return 'none'
