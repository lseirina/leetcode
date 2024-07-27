def max_profit(prices):
    min_price = min(prices)
    for i in range(len(prices)):
        if prices[i] == min_price:
            max_price = max(prices[i:])

    return max_price - min_price



prices = [7, 1, 5, 3, 6, 4]
profit = max_profit(prices)
print(profit)