# Your original solution for reference.
def maxProfit(prices):
    l, r = 0, 1  # l: buy index, r: sell index
    maxP = 0
    while r < len(prices):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            maxP = max(maxP, profit)
        else:
            l = r
        r += 1
    return maxP
