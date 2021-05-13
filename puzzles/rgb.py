"""
Given an array of strictly the characters 'R', 'G', and 'B',
segregate the values of the array so that all the Rs come first,
the Gs come second, and the Bs come last. You can only swap elements of
the array.

Do this in linear time and in-place.

For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'],
it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].
"""
def rgb(values):
    """
    This function takes an array of 'R', 'G', 'B' values and orders them
    in linear time, in-situ by swapping elements.

    values - the array to manipulate
    """
    pos = 0
    end = len(values)
    while (pos < end):
        value = values[pos]
        if value == 'R':
            # pop out the entry
            values.pop(pos)
            # put it at the beginning of the list
            values.insert(0, value)
            # move onto the next value
            pos += 1
        elif value == 'B':
            # pop out the entry
            values.pop(pos)
            # put it at the end of the list
            values.insert(end, value)
            # we no longer need to process this far
            end -= 1
            # we do not move forward as the next value is now here
        else:
            # nothing changes move onto next value
            pos += 1

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

        def _gen_random_values(self, size):
            values = []
            choices = "RGB"
            for i in range(0, size):
                values.append(
                    random.choice(choices)
                )
            return values
            
        def test_example(self):
            self._check_values("GBRRBRG", "RRRGGBB")

        def test_timings(self):
            print()
            random.seed("12345") # make this reproducible
            for size in (10, 100, 1000, 10000, 100000):
                values = self._gen_random_values(size)
                start = time.perf_counter()
                rgb(values)
                end = time.perf_counter()
                delta = (end - start) * 1000
                print(f"{size:10}: {delta:0.2f} ms [{delta/size:0.3f} ms/value]")
            
    unittest.main()
