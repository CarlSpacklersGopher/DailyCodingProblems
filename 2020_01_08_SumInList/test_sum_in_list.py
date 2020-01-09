import unittest

from sum_in_list import is_sum_in_list


class SumInListTestCase(unittest.TestCase):
    """Tests for 'sum_in_list.py'"""

    def test_example(self):
        """Using the example in the problem statement"""
        self.assertTrue(is_sum_in_list([10, 15, 3, 7], 17))
        self.assertFalse(is_sum_in_list([10, 15, 3, 7], 19))

    def test_k_not_present(self):
        """Purpose: Verify 2 numbers in the list do not sum to k"""
        list_of_numbers = [10, 15, 3, 7]
        k = 12
        self.assertFalse(is_sum_in_list(list_of_numbers, k))

    def test_big_list(self):
        """Purpose: Verify 2 numbers in the list sum to k."""
        list_of_numbers = []
        for i in range(1, 1000):
            list_of_numbers.append(i)
        # Make desired sum the sum of the last 2 numbers to maximize the number of items processed.
        k = list_of_numbers[-1] + list_of_numbers[-2]

        self.assertTrue(is_sum_in_list(list_of_numbers, k))

    def test_negative_sum(self):
        """Purpose: Verify the handling of negative numbers"""
        self.assertTrue(is_sum_in_list([-1, 0, 5, 9, -3], -4))

if __name__ == '__main__':
    # Run tests.  Dump output to log.
    log_file_name = 'test_sum_in_list.log'
    with open(log_file_name, 'w') as log_file:
        runner = unittest.TextTestRunner(log_file)
        unittest.main(testRunner=runner)
        print("running tests")

