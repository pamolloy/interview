#!/usr/bin/env python
#
#   apple-stock/solution.py
#

# Examples consisting of the price over time and maximum profit for that period
examples = [
    ([1, 2, 3, 4, 5], 4),
    ([10, 11, 2, 9], 7),
    ([5, 10, 3, 5], 5),
    ([5, 4, 3, 2, 1], 0),   # The price goes down over the entire period
    ([1, 1, 1, 1, 1], 0),   # The price stays the same
    ([1], 0)
]

def best_profit_lowest(stock_prices_yesterday):
    """Find the best profit based on the day's lowest price. Note that this
       may not be the maximum profit for the day (e.g. [5, 10, 3, 5])"""

    min_price = max_price = stock_prices_yesterday[0]

    for price in stock_prices_yesterday:
        if price < min_price:
            min_price = price
            # We only want to maximum price after the minimum price was found
            max_price = price
        elif price > max_price:
            max_price = price

    return max_price - min_price

def best_profit_brute(stock_prices_yesterday):
    """Compare the value at each time with the values at the following times and
       find the greatest difference. Unfortunately, the two for loops result in
       O(n^2) time."""

    min_index = max_index = delta = 0

    for index, price in enumerate(stock_prices_yesterday):
        for next_index, next_price in enumerate(stock_prices_yesterday[index:]):
            next_delta = next_price - price
            if next_delta > delta:
                min_index = index
                max_index = next_index
                delta = next_delta

    # If the price decreases over the entire period no profit can be made
    if delta < 0:
        delta = 0

    return delta

def best_profit(stock_prices_yesterday):
    """With every value check if it is a relative low or whether it results in
       a greater delta. Only looping through once results in O(n) time."""

    delta = 0
    min_price = stock_prices_yesterday[0]

    for index, price in enumerate(stock_prices_yesterday):
        if price < min_price:
            min_price = price
        elif (price - min_price) > delta:
            delta = price - min_price

    return delta

if __name__ == "__main__":
    for solve in [best_profit_lowest, best_profit_brute, best_profit]:
        print("Solution: {name}\n{doc}\n".format(
                name=solve.__name__, doc=solve.__doc__))
        for prices, solution in examples:
            try:
                result = solve(prices)
                message = "Example: {example}\nResult: {result}\nSolution: {solution}".format(
                        example=prices, result=result, solution=solution)
                assert solution == result
                print("{0}\nSUCCESS\n".format(message))
            except AssertionError:
                print("{0}\nFAILURE\n".format(message))

