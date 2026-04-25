class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        sum = 0
        current = 0
        max = 0
        for g in gain:
            current = current + g
            if current > max:
                max = current
            
        return max









        
