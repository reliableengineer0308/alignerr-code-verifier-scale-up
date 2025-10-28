import unittest
from solution import longest_repeating_substring

class TestLongestRepeatingSubstring(unittest.TestCase):

    def test_no_repeating(self):
        self.assertEqual(longest_repeating_substring("abcd"), 0)
        self.assertEqual(longest_repeating_substring("abcdef"), 0)
        self.assertEqual(longest_repeating_substring("a"), 0)

    def test_single_char_repeated(self):
        self.assertEqual(longest_repeating_substring("aaaa"), 3)
        self.assertEqual(longest_repeating_substring("zzzzz"), 4)

    def test_example_1(self):
        self.assertEqual(longest_repeating_substring("abbaba"), 2)

    def test_example_2(self):
        self.assertEqual(longest_repeating_substring("aabcaabdaab"), 3)

    def test_overlapping_occurrences(self):
        # "aaa! appears at [0,1,2] and [1,2,3]
        self.assertEqual(longest_repeating_substring("aaaaa"), 4)
        self.assertEqual(longest_repeating_substring("aaabaaa"), 3)  # "aaa" repeats

    def test_long_string(self):
        s = "abcabcabcabc"  # "abcabc! repeats?
        # Actually, "abc! repeats many times, but longest is "abcabc" (length 6)
        # Occurrences: [0:6] and [6:12]
        self.assertEqual(longest_repeating_substring(s), 9)

    def test_edge_cases(self):
        self.assertEqual(longest_repeating_substring(""), 0)
        self.assertEqual(longest_repeating_substring("xy"), 0)  # no repeat
        self.assertEqual(longest_repeating_substring("xx"), 1)  # "x" repeats

if __name__ == '__main__':
    unittest.main()
