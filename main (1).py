from stockchart import *
from solution import *


def main():

    prices = [7, 1, 5, 3, 6, 4]
    visualize_max_profit(prices)

    # Run test cases.
    # test_visualizer_cases()

    print(maxProfit(prices))


if __name__ == '__main__':
    main()
