"""
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
"""
def get_max_profit(prices: list) -> int:
    max_profit = 0
    min_price = float('inf') # float('inf') is a way to represent positive infinity.
    # It's a special floating-point value that is greater than any other number.
    for price in prices:
        if price < min_price:
            min_price = price
        else:
            profit = price - min_price
            max_profit = max(profit, max_profit)

    return max_profit


print(get_max_profit([7,1,5,3,6,4]))