class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf') # Start infinitely high
        max_profit = 0
        
        for price in prices:
            if price < min_price:
                # We found a new lowest price to buy at
                min_price = price
            elif price - min_price > max_profit:
                # We found a better profit to sell at
                max_profit = price - min_price
                
        return max_profit