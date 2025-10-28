import unittest
from solution import greedy_coin_change

class TestGreedyCoinChange(unittest.TestCase):

    def test_basic_usd_coins(self):
        """Standard US coin system."""
        coins = [1, 5, 10, 25]
        self.assertEqual(greedy_coin_change(coins, 67), 6)  # 2×25 + 1×10 + 1×5 + 2×1

    def test_amount_zero(self):
        """Zero amount requires zero coins."""
        self.assertEqual(greedy_coin_change([1, 5], 0), 0)

    def test_single_coin(self):
        """Only one coin type."""
        self.assertEqual(greedy_coin_change([1], 10), 10)
        self.assertEqual(greedy_coin_change([5], 15), 3)

    def test_non_canonical_system(self):
        """Greedy may not be optimal, but we return greedy result."""
        coins = [1, 3, 4]
        # Greedy for 6: 4 + 1 + 1 → 3 coins (optimal is 3+3 → 2 coins)
        self.assertEqual(greedy_coin_change(coins, 6), 3)

    def test_exact_fit(self):
        """Amount exactly divisible by a coin."""
        coins = [1, 2, 5]
        self.assertEqual(greedy_coin_change(coins, 10), 2)  # 2×5

    def test_large_amount(self):
        """Large amount with mixed coins."""
        coins = [1, 10, 50, 100]
        self.assertEqual(greedy_coin_change(coins, 999), 23)  # 9×100 + 1×50 + 4×10 + 9×1

    def test_invalid_amount(self):
        """Negative amount should return -1."""
        self.assertEqual(greedy_coin_change([1, 5], -5), -1)

    def test_empty_coins(self):
        """Empty coin list → impossible unless amount=0."""
        self.assertEqual(greedy_coin_change([], 5), -1)
        self.assertEqual(greedy_coin_change([], 0), 0)


if __name__ == '__main__':
    unittest.main()
