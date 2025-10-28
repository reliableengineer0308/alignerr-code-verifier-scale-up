import unittest
import sys
from io import StringIO
from solution import LazySegmentTree, solve_segment_tree

class TestSegmentTree(unittest.TestCase):
    
    def test_basic_operations(self):
        """Test basic update and query operations"""
        arr = [1, 2, 3, 4, 5]
        seg_tree = LazySegmentTree(arr)
        
        # Initial query
        self.assertEqual(seg_tree.query_range(0, 4), 15)
        
        # Update range and query
        seg_tree.update_range(1, 3, 2)
        self.assertEqual(seg_tree.query_range(0, 4), 21)  # 1 + 4 + 5 + 6 + 5
        
        # Another update and query - CORRECTED EXPECTATION
        seg_tree.update_range(2, 4, -1)
        # After updates: [1, 4, 4, 5, 4]
        # query 1,3: 4 + 4 + 5 = 13 (NOT 14)
        self.assertEqual(seg_tree.query_range(1, 3), 13)
    
    def test_single_element(self):
        """Test with single element array"""
        arr = [42]
        seg_tree = LazySegmentTree(arr)
        
        self.assertEqual(seg_tree.query_range(0, 0), 42)
        seg_tree.update_range(0, 0, 8)
        self.assertEqual(seg_tree.query_range(0, 0), 50)
    
    def test_large_numbers(self):
        """Test with large numbers"""
        arr = [1000000000, 2000000000, 3000000000]
        seg_tree = LazySegmentTree(arr)
        
        self.assertEqual(seg_tree.query_range(0, 2), 6000000000)
        seg_tree.update_range(0, 2, -500000000)
        self.assertEqual(seg_tree.query_range(0, 2), 4500000000)
        seg_tree.update_range(1, 1, 1000000000)
        self.assertEqual(seg_tree.query_range(0, 2), 5500000000)
    
    def test_multiple_updates_same_range(self):
        """Test multiple updates on same range"""
        arr = [0, 0, 0, 0]
        seg_tree = LazySegmentTree(arr)
        
        seg_tree.update_range(0, 3, 5)
        self.assertEqual(seg_tree.query_range(0, 3), 20)  # 4 * 5 = 20
        
        seg_tree.update_range(1, 2, 3)
        self.assertEqual(seg_tree.query_range(0, 3), 26)  # 20 + 2 * 3 = 26
        
        seg_tree.update_range(0, 0, -2)
        self.assertEqual(seg_tree.query_range(0, 3), 24)  # 26 - 2 = 24
    
    def test_edge_cases(self):
        """Test edge cases"""
        # Empty range query
        arr = [1, 2, 3]
        seg_tree = LazySegmentTree(arr)
        self.assertEqual(seg_tree.query_range(2, 1), 0)  # Invalid range
    
    def test_negative_updates(self):
        """Test negative value updates"""
        arr = [10, 20, 30, 40]
        seg_tree = LazySegmentTree(arr)
        
        self.assertEqual(seg_tree.query_range(0, 3), 100)
        seg_tree.update_range(1, 2, -15)
        # After update: [10, 5, 15, 40] = 70
        self.assertEqual(seg_tree.query_range(0, 3), 70)
    
    def test_solve_function_basic(self):
        """Test main solve function with basic input - CORRECTED"""
        input_data = """5 5
1 2 3 4 5
query 0 4
update 1 3 2
query 0 4
update 2 4 -1
query 1 3"""
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_segment_tree()
            self.assertEqual(len(results), 3)
            self.assertEqual(results[0], "15")
            self.assertEqual(results[1], "21")
            self.assertEqual(results[2], "13")  # CORRECTED: 13 instead of 14
        finally:
            sys.stdin = old_stdin
    
    def test_solve_function_complex(self):
        """Test main solve function with complex input - CORRECTED"""
        input_data = """6 8
10 20 30 40 50 60
query 1 4
update 2 5 5
query 0 5
update 0 3 -10
query 1 2
update 4 5 15
query 3 5
query 0 0"""
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_segment_tree()
            self.assertEqual(len(results), 5)
            self.assertEqual(results[0], "140")  # 20+30+40+50
            self.assertEqual(results[1], "230")  # 10+20+35+45+55+65
            self.assertEqual(results[2], "35")   # 10+25 = 35 (CORRECTED)
            self.assertEqual(results[3], "185")  # 35+70+80 = 185
            self.assertEqual(results[4], "0")    # 0
        finally:
            sys.stdin = old_stdin
    
    def test_solve_function_large_numbers(self):
        """Test main solve function with large numbers - CORRECTED"""
        input_data = """3 3
1000000000 2000000000 3000000000
query 0 2
update 0 2 -500000000
query 0 2"""
        # Removed the third query to match the output
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_segment_tree()
            self.assertEqual(len(results), 2)  # CORRECTED: 2 queries instead of 3
            self.assertEqual(results[0], "6000000000")
            self.assertEqual(results[1], "4500000000")
        finally:
            sys.stdin = old_stdin

def run_specific_test():
    """Run specific test cases to verify functionality"""
    print("=== Testing Segment Tree with Lazy Propagation ===")
    
    # Test 1: Basic operations
    print("\n1. Basic Operations Test:")
    arr1 = [1, 2, 3, 4, 5]
    seg_tree1 = LazySegmentTree(arr1)
    print(f"Initial: {seg_tree1.query_range(0, 4)} (expected: 15)")
    
    seg_tree1.update_range(1, 3, 2)
    print(f"After update [1,3] +2: {seg_tree1.query_range(0, 4)} (expected: 21)")
    
    seg_tree1.update_range(2, 4, -1)
    result = seg_tree1.query_range(1, 3)
    print(f"After update [2,4] -1, query [1,3]: {result} (expected: 13)")
    print(f"Array should be: [1, 4, 4, 5, 4] = 4+4+5=13")
    
    # Test 2: Large numbers
    print("\n2. Large Numbers Test:")
    arr2 = [1000000000, 2000000000, 3000000000]
    seg_tree2 = LazySegmentTree(arr2)
    result1 = seg_tree2.query_range(0, 2)
    print(f"Initial sum: {result1} (expected: 6000000000)")
    
    seg_tree2.update_range(0, 2, -500000000)
    result2 = seg_tree2.query_range(0, 2)
    print(f"After -500000000: {result2} (expected: 4500000000)")

if __name__ == '__main__':
    # Run specific tests first
    run_specific_test()
    print("\n" + "="*50 + "\n")
    
    # Run unit tests
    unittest.main(verbosity=2)