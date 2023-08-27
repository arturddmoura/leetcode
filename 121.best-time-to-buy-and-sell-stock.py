#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        highest_sale_price = prices[-1]
        highest_profit = 0

        for stock_price in reversed(prices):
            if stock_price > highest_sale_price:
                highest_sale_price = stock_price
            if highest_profit < highest_sale_price - stock_price:
                highest_profit = highest_sale_price - stock_price

        return highest_profit
# @lc code=end

solution = Solution()
solution.maxProfit(prices = [2,4,1])
solution.maxProfit(prices = [7,1,5,3,6,4])
