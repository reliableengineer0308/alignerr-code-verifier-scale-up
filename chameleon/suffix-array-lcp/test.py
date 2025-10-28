import unittest
import sys
from io import StringIO
from solution import solve_suffix_array, build_suffix_array, build_lcp_array

class TestSuffixArray(unittest.TestCase):
    
    def test_basic_suffix_array(self):
        """Test suffix array construction"""
        s = "banana"
        suffix = build_suffix_array(s)
        expected = [5, 3, 1, 0, 4, 2]  # a, ana, anana, banana, na, nana
        self.assertEqual(suffix, expected)
    
    def test_basic_lcp(self):
        """Test LCP array construction"""
        s = "banana"
        suffix = [5, 3, 1, 0, 4, 2]
        lcp = build_lcp_array(s, suffix)
        expected = [0, 1, 3, 0, 0, 2]
        self.assertEqual(lcp, expected)
    
    def test_example_1(self):
        """Test example 1 from prompt"""
        input_data = """banana
5
LCP 0 1
LCP 1 2
KTH 1
KTH 5
KTH 10"""
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_suffix_array()
            self.assertEqual(len(results), 5)
            self.assertEqual(results[0], "1")  # LCP(0,1)
            self.assertEqual(results[1], "3")  # LCP(1,2)
            self.assertEqual(results[2], "a")  # KTH 1
            self.assertEqual(results[3], "anana")  # KTH 5
            self.assertEqual(results[4], "banan")  # KTH 10
        finally:
            sys.stdin = old_stdin
    
    def test_example_2(self):
        """Test example 2 from prompt"""
        input_data = """abab
4
LCP 0 1
LCP 1 2
KTH 3
KTH 6"""
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_suffix_array()
            self.assertEqual(len(results), 4)
            self.assertEqual(results[0], "2")  # LCP(0,1)
            self.assertEqual(results[1], "0")  # LCP(1,2)
            self.assertEqual(results[2], "aba")  # KTH 3
            self.assertEqual(results[3], "ba")  # KTH 6
        finally:
            sys.stdin = old_stdin
    
    def test_single_character(self):
        """Test single character string"""
        input_data = """a
3
LCP 0 0
KTH 1
KTH 2"""
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_suffix_array()
            self.assertEqual(len(results), 3)
            self.assertEqual(results[0], "1")  # LCP of "a" with itself
            self.assertEqual(results[1], "a")  # First distinct substring
        finally:
            sys.stdin = old_stdin
    
    def test_empty_string(self):
        """Test empty string"""
        input_data = ""
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_suffix_array()
            self.assertEqual(results, [])
        finally:
            sys.stdin = old_stdin

def run_specific_test():
    """Run specific test to verify implementation"""
    test_input = """banana
5
LCP 0 1
LCP 1 2
KTH 1
KTH 5
KTH 10"""
    
    print("=== Running Suffix Array Test ===")
    old_stdin = sys.stdin
    sys.stdin = StringIO(test_input)
    
    try:
        results = solve_suffix_array()
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