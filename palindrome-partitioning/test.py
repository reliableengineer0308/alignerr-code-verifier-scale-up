import unittest
from solution import partition, format_partitions

class TestPalindromePartitioning(unittest.TestCase):
    
    def test_complex_palindrome_pattern(self):
        s = "abacaba"
        result = partition(s)
        expected_solutions = [
            ["a", "b", "a", "c", "a", "b", "a"],
            ["a", "b", "a", "c", "aba"],
            ["a", "b", "aca", "b", "a"],
            ["a", "bacab", "a"],
            ["aba", "c", "a", "b", "a"],
            ["aba", "c", "aba"],
            ["abacaba"]
        ]
        self.assertEqual(len(result), len(expected_solutions))
        for sol in expected_solutions:
            self.assertIn(sol, result)
    
    def test_complex_mixed_pattern(self):
        s = "racecar"
        result = partition(s)
        expected_solutions = [
            ["r", "a", "c", "e", "c", "a", "r"],
            ["r", "a", "cec", "a", "r"],
            ["r", "aceca", "r"],
            ["racecar"]
        ]
        self.assertEqual(len(result), len(expected_solutions))
        for sol in expected_solutions:
            self.assertIn(sol, result)
    
    def test_symmetric_palindrome(self):
        s = "noon"
        result = partition(s)
        expected_solutions = [
            ["n", "o", "o", "n"],
            ["n", "oo", "n"],
            ["noon"]
        ]
        self.assertEqual(len(result), len(expected_solutions))
        for sol in expected_solutions:
            self.assertIn(sol, result)
    
    def test_single_character(self):
        s = "a"
        result = partition(s)
        expected = [["a"]]
        self.assertEqual(result, expected)
    
    def test_all_same_characters(self):
        s = "aaa"
        result = partition(s)
        expected_solutions = [
            ["a", "a", "a"],
            ["a", "aa"],
            ["aa", "a"], 
            ["aaa"]
        ]
        self.assertEqual(len(result), len(expected_solutions))
        for sol in expected_solutions:
            self.assertIn(sol, result)
    
    def test_format_partitions(self):
        partitions = [["a", "b", "a", "c", "a", "b", "a"], ["abacaba"]]
        formatted = format_partitions(partitions)
        self.assertIn("a b a c a b a", formatted)
        self.assertIn("abacaba", formatted)
        self.assertTrue("|" in formatted)
    
    def test_empty_string(self):
        s = ""
        result = partition(s)
        self.assertEqual(result, [[]])

if __name__ == '__main__':
    unittest.main()