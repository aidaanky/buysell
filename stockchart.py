import matplotlib.pyplot as plt


def visualize_max_profit(prices, pause_time=0.8):
    """
    Visualizes the process of finding the maximum profit in the stock prices.
    Uses two pointers: l (buy day) and r (sell day).
    """
    l, r = 0, 1  # l is the candidate buy day, r is the candidate sell day
    maxP = 0

    # Set up the plot.
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(prices,
            marker='o',
            linestyle='-',
            color='blue',
            label='Stock Price')
    ax.set_title("Best Time to Buy and Sell Stock Visualization")
    ax.set_xlabel("Day")
    ax.set_ylabel("Price")
    ax.grid(True)

    # Markers for current buy and sell days.
    buy_marker, = ax.plot([], [], 'go', markersize=10, label='Buy Day')
    sell_marker, = ax.plot([], [], 'ro', markersize=10, label='Sell Day')

    # Annotation for details.
    info_text = ax.text(0.02,
                        0.95,
                        '',
                        transform=ax.transAxes,
                        verticalalignment='top',
                        bbox=dict(facecolor='white', alpha=0.7))
    ax.legend()

    # Turn on interactive mode.
    plt.ion()
    plt.show()

    while r < len(prices):
        # Update markers with sequences (x and y values as lists).
        buy_marker.set_data([l], [prices[l]])
        sell_marker.set_data([r], [prices[r]])

        # Check if the current pair yields a profit.
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            maxP = max(maxP, profit)
            current_profit = profit
        else:
            # Reset buy pointer if no profit.
            l = r
            buy_marker.set_data([l], [prices[l]])
            current_profit = 0

        # Update the annotation with current details.
        info_text.set_text(f"Buy Day (l): {l}\n"
                           f"Sell Day (r): {r}\n"
                           f"Current Profit: {current_profit}\n"
                           f"Max Profit So Far: {maxP}")

        plt.draw()
        plt.pause(pause_time)
        r += 1

    # Finalize the plot.
    plt.ioff()
    plt.show()
    print("Max Profit (Visualized):", maxP)
    return maxP


def test_visualizer_cases():
    """
    Run multiple test cases to check the visualizer on different inputs.
    """
    test_cases = [{
        "prices": [7, 1, 5, 3, 6, 4],
        "description": "Normal case: profit 5 (buy at 1, sell at 6)"
    }, {
        "prices": [7, 6, 4, 3, 1],
        "description": "Decreasing prices: no profit, profit 0"
    }, {
        "prices": [1, 2, 3, 4, 5],
        "description":
        "Increasing prices: profit 4 (buy at 1, sell at 5)"
    }, {
        "prices": [3, 2, 6, 1, 4],
        "description":
        "Mixed prices: best profit 4 (buy at 2, sell at 6)"
    }, {
        "prices": [5, 2, 8, 1, 9, 2, 11, 3],
        "description":
        "Multiple peaks: best profit 10 (buy at 1, sell at 11)"
    }, {
        "prices": [5, 5, 5, 5, 5],
        "description": "Constant prices: no profit, profit 0"
    }]

    for case in test_cases:
        print("\nTesting case:", case["description"])
        visualize_max_profit(case["prices"])
        input("Press Enter to continue to the next test case...")
