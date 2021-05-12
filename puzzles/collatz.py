#
# A Collatz sequence in mathematics can be defined as follows.
# Starting with any positive integer:
#   if n is even, the next number in the sequence is n / 2
#   if n is odd, the next number in the sequence is 3n + 1
#
# It is conjectured that every such sequence eventually reaches the number 1.
# Test this conjecture.
#
# Bonus: What input n <= 1000000 gives the longest sequence?

def _getNextValue(n):
    """
    This function returns the next integer in a Collatz sequence
    
    n - the current number
    """
    if (n % 2):
        # odd number
        return int(3 * n + 1)
    else:
        # even number
        return int(n / 2)

def collatz(value):
    """
    This function returns a collatz sequence for a given number
   
    value - the number to evaluate
    """
    sequence = [value]
    n = value
    while(True):
        n = _getNextValue(n)
        sequence.append(n)
        if n == 1:
            break
    return sequence

def getLargest(maxValue):
    """
    This function will return the largest sequence less than the given maximum.

    maxValue - the maximum value to test
    """
    largest = []
    for i in range(1, maxValue):
        result = collatz(i)
        if len(result) > len(largest):
            largest = result
    return largest

if __name__ == '__main__':
    import unittest

    class TestCollatzMethods(unittest.TestCase):

        def test_collatz_10(self):
            self.assertEqual(
                collatz(10),
                [10,5,16,8,4,2,1]
            )

        def test_collatz_78(self):
            self.assertEqual(
                collatz(78),
                [78,39,118,59,178,89,268,134,67,202,101,304,152,76,
                 38,19,58,29,88,44,22,11,34,17,52,26,13,40,20,10,
                 5,16,8,4,2,1]
            )

        def test_getLargest_100(self):
            largest = getLargest(100)
            self.assertEqual(
                len(largest), 119
            )
            print(f"Largest ({len(largest)} values): {largest}")
            

    unittest.main()
