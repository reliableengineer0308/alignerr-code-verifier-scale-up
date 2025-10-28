import unittest
from solution import count_unique_permutations

class TestUniquePermutations(unittest.TestCase):

    def test_empty_string(self):
        """Empty string has 1 permutation."""
        self.assertEqual(count_unique_permutations(""), 1)

    def test_single_character(self):
        """Single character has 1 permutation."""
        self.assertEqual(count_unique_permutations("a"), 1)
        self.assertEqual(count_unique_permutations(["x"]), 1)

    def test_all_unique(self):
        """All characters distinct → n# permutations."""
        self.assertEqual(count_unique_permutations("abc"), 6)   # 3! = 6
        self.assertEqual(count_unique_permutations("abcd"), 24) # 4! = 24

    def test_with_duplicates(self):
        """String with repeated characters."""
        self.assertEqual(count_unique_permutations("aab"), 3)   # 3!/2! = 3
        self.assertEqual(count_unique_permutations("aabb"), 6)  # 4!/(2!2!) = 6
        self.assertEqual(count_unique_permutations("aaab"), 4)   # 4!/3! = 4

    def test_all_same(self):
        """All characters identical → only 1 permutation."""
        self.assertEqual(count_unique_permutations("aaa"), 1)
        self.assertEqual(count_unique_permutations("zzzzz"), 1)

    def test_two_chars_mixed(self):
        """Two different characters with repeats."""
        self.assertEqual(count_unique_permutations("ab"), 2)    # 2! = 2
        self.assertEqual(count_unique_permutations("abb"), 3)     # 3!/2! = 3

    def test_case_sensitive(self):
        """Case sensitivity: 'A' ≠ 'a'."""
        self.assertEqual(count_unique_permutations("Aa"), 2)      # 'Aa', 'aA'
        self.assertEqual(count_unique_permutations("AAa"), 3)   # 3!/2! = 3

    def test_longer_with_repeats(self):
        """Longer string with multiple repeats."""
        # "aabbcc! → 6! / (2!2!2!) = 720 / 8 = 90
        self.assertEqual(count_unique_permutations("aabbcc"), 90)

if __name__ == '__main__':
    unittest.main()
