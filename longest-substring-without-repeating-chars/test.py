import unittest
from solution import length_of_longest_substring

class TestLongestSubstring(unittest.TestCase):

    def test_example_1(self):
        """Test case with repeating pattern."""
        self.assertEqual(length_of_longest_substring("abcabcbb"), 3)

    def test_all_same(self):
        """Test string with all identical characters."""
        self.assertEqual(length_of_longest_substring("bbbbb"), 1)

    def test_mixed_repeats(self):
        """Test with scattered repeats."""
        self.assertEqual(length_of_longest_substring("pwwkew"), 3)

    def test_empty_string(self):
        """Test empty input."""
        self.assertEqual(length_of_longest_substring(""), 0)

    def test_single_char(self):
        """Test single character."""
        self.assertEqual(length_of_longest_substring("a"), 1)

    def test_no_repeats(self):
        """Test string with no repeating characters."""
        self.assertEqual(length_of_longest_substring("abcdef"), 6)

    def test_long_with_repeats(self):
        """Test longer string with complex repeats."""
        s = "abcdeafghijklmnopqrstuvwxyz"
        # 'a' repeats, but rest are unique → longest = "bcdeafghijk..."
        self.assertEqual(length_of_longest_substring(s), 26)

    def test_special_chars(self):
        """Test with digits and symbols."""
        self.assertEqual(length_of_longest_substring("123#@"), 5)  # "123#@"

if __name__ == "__main__":
    unittest.main()
