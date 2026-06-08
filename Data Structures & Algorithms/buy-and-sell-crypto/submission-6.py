class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        pointer1=0
        pointer2=1
        i=0
        while pointer2!=len(prices):
            
            if prices[pointer1]>prices[pointer2]:
                pointer1=pointer2
                pointer2+=1
                       
            else:
                if profit<prices[pointer2]-prices[pointer1]:
                    profit=prices[pointer2]-prices[pointer1]
                pointer2+=1
            
        return profit


        