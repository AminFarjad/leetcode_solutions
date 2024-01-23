class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        a=[0]
        i=1
        ma=prices[0]
        while i < len(prices):
            
            a.append(max(a[i-1],prices[i]-prices[i-1],prices[i]-ma))
            if ma > prices[i]:
                ma=prices[i]
            i+=1
        return a[-1]
