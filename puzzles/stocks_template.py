"""
Given an array of numbers representing the stock prices of a company
in chronological order and an integer k, return the maximum profit you
can make from k buys and sells.

You must buy the stock before you can sell it,
and you must sell the stock before you can buy it again.

For example, given k = 2 and the array [5, 2, 4, 0, 1], you should return 3.
"""
def stocks(values, maxSales):
    """
    This function evaluates the maximum profit that could be achieved through
    the purchase and sale of stock over a period of time.
 
    values   - the stock values over time
    maxSales - the maximum number of sales 
    """
    return 0

if __name__ == '__main__':
    import unittest

    class TestStocks(unittest.TestCase):

        def test_example(self):
            self.assertEqual(
                stocks([5,2,4,0,1], 2),
                3
            )
                
    unittest.main()
