import unittest
import sys
from io import StringIO
from solution import solve_palindromic_tree, SimplePalindromicSolver

class TestPalindromicTree(unittest.TestCase):
    
    def test_example_1(self):
        """Test example 1 from prompt"""
        input_data = """ababa
6
COUNT
LONGEST
FREQ 1
FREQ 2
KTH 3
KTH 5"""
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_palindromic_tree()
            self.assertEqual(len(results), 6)
            self.assertEqual(results[0], "5")     # COUNT
            self.assertEqual(results[1], "ababa") # LONGEST
            self.assertEqual(results[2], "3")     # FREQ 1 ("a" occurs 3 times)
            self.assertEqual(results[3], "2")     # FREQ 2 ("aba" occurs 2 times)
            self.assertEqual(results[4], "ababa") # KTH 3
            self.assertEqual(results[5], "bab")   # KTH 5
        finally:
            sys.stdin = old_stdin
    
    def test_example_2(self):
        """Test example 2 from prompt"""
        input_data = """abcba
5
COUNT
LONGEST
KTH 1
KTH 4
FREQ 3"""
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_palindromic_tree()
            self.assertEqual(len(results), 5)
            self.assertEqual(results[0], "5")     # COUNT
            self.assertEqual(results[1], "abcba") # LONGEST
            self.assertEqual(results[2], "a")     # KTH 1
            self.assertEqual(results[3], "bcb")   # KTH 4
            self.assertEqual(results[4], "2")     # FREQ 3 ("b" occurs 2 times)
        finally:
            sys.stdin = old_stdin
    
    def test_single_character(self):
        """Test single character string"""
        input_data = """a
3
COUNT
LONGEST
KTH 1"""
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_palindromic_tree()
            self.assertEqual(len(results), 3)
            self.assertEqual(results[0], "1")  # COUNT: only "a"
            self.assertEqual(results[1], "a")  # LONGEST: "a"
            self.assertEqual(results[2], "a")  # KTH 1: "a"
        finally:
            sys.stdin = old_stdin
    
    def test_no_palindrome(self):
        """Test string with no palindromes longer than 1"""
        input_data = """abc
3
COUNT
LONGEST
KTH 1"""
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_palindromic_tree()
            self.assertEqual(len(results), 3)
            self.assertEqual(results[0], "3")  # COUNT: "a", "b", "c"
            self.assertEqual(results[1], "a")  # LONGEST: single characters
            self.assertEqual(results[2], "a")  # KTH 1: "a"
        finally:
            sys.stdin = old_stdin
    
    def test_empty_string(self):
        """Test empty string"""
        input_data = """
1
COUNT"""
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_palindromic_tree()
            self.assertEqual(results[0], "0")  # COUNT: 0 palindromes
        finally:
            sys.stdin = old_stdin

def run_specific_test():
    """Run specific test to verify implementation"""
    test_input = """ababa
6
COUNT
LONGEST
FREQ 1
FREQ 2
KTH 3
KTH 5"""
    
    print("=== Running Palindromic Tree Test ===")
    old_stdin = sys.stdin
    sys.stdin = StringIO(test_input)
    
    try:
        results = solve_palindromic_tree()
        print("Results:")
        for i, result in enumerate(results, 1):
            print(f"Test {i}: {result}")
    finally:
        sys.stdin = old_stdin

if __name__ == '__main__':
    # Run specific test first
    run_specific_test()
    print("\n" + "="*50 + "\n")
    
    # Run unit tests
    unittest.main(verbosity=2)