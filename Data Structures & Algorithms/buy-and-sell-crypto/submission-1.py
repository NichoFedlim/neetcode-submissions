class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # max_profit = 0
        # for i in range (len(prices)):
        #     for j in range (i+1, len(prices)):
        #         profit = prices[j] - prices[i]
                
        #         if max_profit < profit:
        #             max_profit = profit
        #             print(max_profit)
        #         else:
        #             continue
        # return max_profit

        min_price = sys.maxsize       # cheapest price seen so far
        max_profit = 0                  # best profit found so far

        for price in prices:
            if price < min_price:
                min_price = price              # found a cheaper buy day
            elif price - min_price > max_profit:
                max_profit = price - min_price # found a better sell day

        return max_profit