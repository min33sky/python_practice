# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
from typing import List
from sys import maxsize


def maxProfit(prices: List[int]) -> int:
    profit = 0
    min_price = maxsize

    # 최소값과 최대값을 계속 갱신
    for price in prices:
        min_price = min(price, min_price)
        profit = max(profit, price - min_price)

    return profit


print(maxProfit([7, 1, 5, 3, 6, 4]))
