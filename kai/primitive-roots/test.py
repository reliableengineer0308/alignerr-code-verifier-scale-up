import unittest
import sys
from io import StringIO
from solution import PrimitiveRootFinder, solve_primitive_roots

class TestPrimitiveRoots(unittest.TestCase):
    
    def test_basic_cases(self):
        finder = PrimitiveRootFinder(100)
        
        self.assertEqual(finder.find_smallest_primitive_root(2), 1)
        self.assertEqual(finder.find_smallest_primitive_root(3), 2)
        self.assertEqual(finder.find_smallest_primitive_root(5), 2)
        self.assertEqual(finder.find_smallest_primitive_root(7), 3)
        self.assertEqual(finder.find_smallest_primitive_root(11), 2)
    
    def test_known_primes(self):
        finder = PrimitiveRootFinder(1000)
        
        self.assertEqual(finder.find_smallest_primitive_root(13), 2)
        self.assertEqual(finder.find_smallest_primitive_root(17), 3)
        self.assertEqual(finder.find_smallest_primitive_root(19), 2)
        self.assertEqual(finder.find_smallest_primitive_root(23), 5)
    
    def test_larger_primes(self):
        finder = PrimitiveRootFinder(1100000)
        
        # For prime 1000003, smallest primitive root is 2
        self.assertEqual(finder.find_smallest_primitive_root(1000003), 2)
    
    def test_full_integration(self):
        input_data = """5
2
3
5
7
11"""
        
        expected_output = ["1", "2", "2", "3", "2"]
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_primitive_roots()
            self.assertEqual(results, expected_output)
        finally:
            sys.stdin = old_stdin

if __name__ == '__main__':
    unittest.main(verbosity=2)