
def check_overflow(reverse,rhs,neg):
        max= 2**31 -1
        min= -2**31

        if (max - reverse*10) < rhs and not neg:
            return True
        
        if neg and (max - reverse*10) +1 < rhs:
            return True
        return False
class Solution:
    
    def reverse(self, x: int) -> int:
        # 2^31
        
        neg = True if x < 0 else False
        reverse = 0
        i=1
        x=abs(x)
        while x > 0:
            mode = x % 10
            if check_overflow(reverse,mode,neg):
                return 0
            reverse =reverse*10+ mode
            print(reverse)
            
            x=x//10
        
        if neg:
            return -reverse
        return reverse
    
    






        
