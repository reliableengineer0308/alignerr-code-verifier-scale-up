import unittest

from solution import solve


class TestThreeItemsInArray(unittest.TestCase):
    def test_one_zero_in_three(self):
        assert solve([5, 6, 0, 4, 0, 1, 2, 0, 2, 5, 1, 2, 1, 1, 3, 4, 2, 3, 2, 3, 4, 3]) == 8

    def test_two_zero_in_three(self):
        assert solve([4, 3, 0, 3, 0, 1, 1, 1, 2, 1, 2, 3, 1]) == 3

    def test_four_items(self):
        assert solve([3, 1, 0, 2, 0, 1, 5]) == -1


if __name__ == "__main__":
    unittest.main()
