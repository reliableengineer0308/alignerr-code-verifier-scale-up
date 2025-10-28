import unittest
import sys
from io import StringIO
from solution import solve_splay_tree, SplayTree, SplayNode

class TestSplayTree(unittest.TestCase):
    
    def test_basic_operations(self):
        """Test basic insert, delete, query operations"""
        input_data = """3 6
10 20 30
INSERT 1 15
QUERY 0 3
DELETE 0
QUERY 0 2
UPDATE 1 25
QUERY 0 1"""
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_splay_tree()
            self.assertEqual(len(results), 3)
            self.assertEqual(results[0], "75")  # 10+15+20+30=75
            self.assertEqual(results[1], "65")  # 15+20+30=65
            self.assertEqual(results[2], "40")  # 15+25=40
        finally:
            sys.stdin = old_stdin
    
    def test_empty_tree(self):
        """Test operations on empty tree"""
        input_data = """0 3
INSERT 0 5
QUERY 0 0
DELETE 0"""
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_splay_tree()
            self.assertEqual(len(results), 1)
            self.assertEqual(results[0], "5")  # Only element is 5
        finally:
            sys.stdin = old_stdin
    
    def test_single_element(self):
        """Test single element operations"""
        input_data = """1 4
100
QUERY 0 0
UPDATE 0 200
QUERY 0 0
DELETE 0"""
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_splay_tree()
            self.assertEqual(results, ["100", "200"])
        finally:
            sys.stdin = old_stdin
    
    def test_complex_sequence(self):
        """Test complex sequence of operations"""
        input_data = """2 7
1 2
QUERY 0 1
INSERT 1 3
QUERY 0 2
DELETE 0
QUERY 0 1
INSERT 0 4
QUERY 0 2"""
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_splay_tree()
            self.assertEqual(len(results), 4)
            self.assertEqual(results[0], "3")   # 1+2=3
            self.assertEqual(results[1], "6")   # 1+3+2=6
            self.assertEqual(results[2], "5")   # 3+2=5
            self.assertEqual(results[3], "9")   # 4+3+2=9
        finally:
            sys.stdin = old_stdin

class TestSplayTreeClass(unittest.TestCase):
    def test_splay_tree_creation(self):
        tree = SplayTree()
        tree.insert(0, 10)
        tree.insert(1, 20)
        self.assertEqual(tree.query_range(0, 1), 30)
        
        tree.update_val(0, 5)
        self.assertEqual(tree.query_range(0, 1), 25)
        
        tree.delete(0)
        self.assertEqual(tree.query_range(0, 0), 20)

def run_specific_test():
    """Run specific test to verify implementation"""
    test_input = """3 6
10 20 30
INSERT 1 15
QUERY 0 3
DELETE 0
QUERY 0 2
UPDATE 1 25
QUERY 0 1"""
    
    print("=== Running Splay Tree Test ===")
    old_stdin = sys.stdin
    sys.stdin = StringIO(test_input)
    
    try:
        results = solve_splay_tree()
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