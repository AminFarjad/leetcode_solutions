class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxo = max(candies)
        return [True if x+extraCandies >= maxo else False for x in candies]
        
