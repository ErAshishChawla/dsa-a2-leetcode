from typing import List


def maxProfit(prices: List[int]) -> int:
    n = len(prices)

    max_profit = float("-inf")

    for i in range(n):
        for j in range(i + 1, n):
            curr_profit = prices[j] - prices[i]
            max_profit = max(max_profit, curr_profit)

    return max_profit if max_profit > 0 else 0


def maxProfit2(prices: List[int]) -> int:
    min_price = float("inf")
    max_profit = 0

    for price in prices:
        # Update the min price
        min_price = min(min_price, price)

        # Calculate current profit
        curr_profit = price - min_price

        # Update the max profit
        max_profit = max(max_profit, curr_profit)

    return max_profit


test_case_1 = [20, 25, 3, 12, 16, 1]

print(maxProfit(test_case_1))  # 13
print(maxProfit2(test_case_1))  # 13
