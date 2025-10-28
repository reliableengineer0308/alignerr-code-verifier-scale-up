import unittest
from solution import longestPalindromicSubstring


class TestLPS(unittest.TestCase):
    def test_example_1(self):
        self.assertIn(longestPalindromicSubstring("babad"), ["bab", "aba"])

    
    def test_example_2(self):
        self.assertEqual(longestPalindromicSubstring("cbbd"), "bb")
    
    
    def test_single_char(self):
        self.assertEqual(longestPalindromicSubstring("a"), "a")
    
    
    def test_no_long_palindrome(self):
        result = longestPalindromicSubstring("abcdef")
        self.assertIn(result, list("abcdef"))  # Any single char
        self.assertEqual(len(result), 1)
    
    
    def test_full_palindrome(self):
        self.assertEqual(longestPalindromicSubstring("racecar"), "racecar")
    
    
    def test_empty_string(self):
        self.assertEqual(longestPalindromicSubstring(""), "")
    
    
    def test_two_chars(self):
        self.assertIn(longestPalindromicSubstring("aa"), ["aa"])
        self.assertIn(longestPalindromicSubstring("ab"), ["a", "b"])
    
    
    def test_long_string(self):
        s = "aabbaaccaaabb"
        result = longestPalindromicSubstring(s)
        self.assertTrue(result == result[::-1])  # Is palindrome
        self.assertGreaterEqual(len(result), 2)

if __name__ == '__main__':
    unittest.main()