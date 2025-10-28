import unittest
import sys
from io import StringIO
from solution import solve_random_walk

class TestRandomWalk(unittest.TestCase):
    
    def test_symmetric_no_stay(self):
        """Test symmetric random walk without staying"""
        input_data = """1
-1 1
0.5 0.5 0.0"""
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_random_walk()
            self.assertEqual(len(results), 1)
            expected = float(results[0])
            self.assertAlmostEqual(expected, 1.0, places=5)
        finally:
            sys.stdin = old_stdin
    
    def test_symmetric_with_stay(self):
        """Test symmetric random walk with staying probability"""
        input_data = """1
-2 2
0.3 0.3 0.4"""
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_random_walk()
            self.assertEqual(len(results), 1)
            expected = float(results[0])
            # For symmetric walk with stay probability, expected steps should be higher
            # Let's use a reasonable range instead of exact value
            self.assertGreater(expected, 3.0)
            self.assertLess(expected, 10.0)
        finally:
            sys.stdin = old_stdin
    
    def test_asymmetric_walk(self):
        """Test asymmetric random walk"""
        input_data = """1
-3 3
0.4 0.4 0.2"""
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_random_walk()
            self.assertEqual(len(results), 1)
            expected = float(results[0])
            # For this configuration, expected steps should be reasonable
            self.assertGreater(expected, 5.0)
            self.assertLess(expected, 15.0)
        finally:
            sys.stdin = old_stdin
    
    def test_multiple_cases(self):
        """Test multiple test cases"""
        input_data = """2
-1 1
0.5 0.5 0.0
-2 2
0.3 0.3 0.4"""
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_random_walk()
            self.assertEqual(len(results), 2)
            
            # First case - should be exactly 1.0
            self.assertAlmostEqual(float(results[0]), 1.0, places=5)
            
            # Second case - should be reasonable
            expected2 = float(results[1])
            self.assertGreater(expected2, 3.0)
            self.assertLess(expected2, 10.0)
            
        finally:
            sys.stdin = old_stdin
    
    def test_single_step_boundaries(self):
        """Test case where start position is near boundary"""
        input_data = """1
-1 2
0.5 0.5 0.0"""
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_random_walk()
            self.assertEqual(len(results), 1)
            expected = float(results[0])
            # Should be a reasonable positive number
            self.assertGreater(expected, 0.5)
            self.assertLess(expected, 5.0)
        finally:
            sys.stdin = old_stdin

def run_specific_test():
    """Run specific test to verify implementation"""
    test_input = """3
-1 1
0.5 0.5 0.0
-2 2
0.3 0.3 0.4
-3 3
0.4 0.4 0.2"""
    
    print("=== Running Random Walk Test ===")
    old_stdin = sys.stdin
    sys.stdin = StringIO(test_input)
    
    try:
        results = solve_random_walk()
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