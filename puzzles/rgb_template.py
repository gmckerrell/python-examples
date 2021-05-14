"""
Given an array of strictly the characters 'R', 'G', and 'B',
segregate the values of the array so that all the Rs come first,
the Gs come second, and the Bs come last. You can only swap elements of
the array.

Do this in linear time and in-place.

For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'],
it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].
"""
def _swap(values, left, right):
    values[left], values[right] = values[right], values[left]
    
def rgb(values):
    """
    This function takes an array of 'R', 'G', 'B' values and orders them
    in linear time, in-situ by swapping elements.

    values - the array to manipulate
    """
    return values

if __name__ == '__main__':
    import unittest
    import time
    import random

    class TestRgb(unittest.TestCase):

        def _check_values(self, value_string, expected_string):
            values = list(value_string)
            expected = list(expected_string)
            rgb(values)
            self.assertEqual(values, expected)

        def test_example(self):
            self._check_values("GBRRBRG", "RRRGGBB")

        def test_start_with_red(self):
            self._check_values("RGBRRBRG", "RRRRGGBB")

        def test_start_with_blue(self):
            self._check_values("BGBRRBRG", "RRRGGBBB")

        def test_end_with_red(self):
            self._check_values("GBRRBRGR", "RRRRGGBB")

        def test_end_with_blue(self):
            self._check_values("GBRRBRGB", "RRRGGBBB")

        def test_timings(self):
            print()
            random.seed("12345") # make this reproducible
            for size in (10, 100, 1000, 10000, 100000, 1000000):
                values = random.choices("RGB", k=size)
                start = time.perf_counter()
                rgb(values)
                end = time.perf_counter()
                delta = (end - start) * 1000
                print(f"{size:10} - {delta:0.2f} ms [{1000 * delta/size:0.4f} us/value]")
            
    unittest.main()
