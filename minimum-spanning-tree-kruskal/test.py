import unittest
import sys
from io import StringIO
from solution import UnionFind, KruskalMST, solve_mst

class TestKruskalMST(unittest.TestCase):
    
    def test_union_find_basic(self):
        """Test basic Union-Find operations"""
        uf = UnionFind(5)
        
        # Initially all elements are separate
        self.assertEqual(uf.find(0), 0)
        self.assertEqual(uf.find(1), 1)
        
        # Union operations
        self.assertTrue(uf.union(0, 1))
        self.assertTrue(uf.union(2, 3))
        
        # Check connections
        self.assertEqual(uf.find(0), uf.find(1))
        self.assertEqual(uf.find(2), uf.find(3))
        self.assertNotEqual(uf.find(0), uf.find(2))
        
        # Union already connected elements
        self.assertFalse(uf.union(0, 1))
    
    def test_simple_connected_graph(self):
        """Test simple connected graph"""
        kruskal = KruskalMST(4)
        kruskal.add_edge(0, 1, 10)
        kruskal.add_edge(0, 2, 6)
        kruskal.add_edge(0, 3, 5)
        kruskal.add_edge(1, 3, 15)
        kruskal.add_edge(2, 3, 4)
        
        result = kruskal.find_mst()
        self.assertEqual(result, 19)
    
    def test_disconnected_graph(self):
        """Test disconnected graph"""
        kruskal = KruskalMST(5)
        kruskal.add_edge(0, 1, 5)
        kruskal.add_edge(1, 2, 3)
        kruskal.add_edge(3, 4, 2)
        
        result = kruskal.find_mst()
        self.assertEqual(result, "Disconnected Graph")
    
    def test_single_vertex(self):
        """Test graph with single vertex"""
        kruskal = KruskalMST(1)
        result = kruskal.find_mst()
        self.assertEqual(result, 0)
    
    def test_complete_graph(self):
        """Test complete graph"""
        kruskal = KruskalMST(4)
        kruskal.add_edge(0, 1, 1)
        kruskal.add_edge(0, 2, 2)
        kruskal.add_edge(0, 3, 3)
        kruskal.add_edge(1, 2, 4)
        kruskal.add_edge(1, 3, 5)
        kruskal.add_edge(2, 3, 6)
        
        result = kruskal.find_mst()
        self.assertEqual(result, 6)
    
    def test_complex_graph(self):
        """Test complex graph with multiple components initially"""
        kruskal = KruskalMST(6)
        kruskal.add_edge(0, 1, 4)
        kruskal.add_edge(0, 2, 3)
        kruskal.add_edge(1, 2, 1)
        kruskal.add_edge(1, 3, 2)
        kruskal.add_edge(2, 3, 4)
        kruskal.add_edge(3, 4, 2)
        kruskal.add_edge(4, 5, 3)
        
        result = kruskal.find_mst()
        self.assertEqual(result, 11)
    
    def test_no_edges(self):
        """Test graph with no edges"""
        kruskal = KruskalMST(3)
        result = kruskal.find_mst()
        self.assertEqual(result, "Disconnected Graph")
    
    def test_duplicate_edges(self):
        """Test graph with duplicate edges"""
        kruskal = KruskalMST(3)
        kruskal.add_edge(0, 1, 5)
        kruskal.add_edge(0, 1, 3)  # Duplicate with lower weight
        kruskal.add_edge(1, 2, 2)
        
        result = kruskal.find_mst()
        self.assertEqual(result, 5)  # 3 + 2
    
    def test_solve_function_single(self):
        """Test main function with single test case"""
        input_data = """1
4 5
0 1 10
0 2 6
0 3 5
1 3 15
2 3 4"""
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_mst()
            self.assertEqual(len(results), 1)
            self.assertEqual(results[0], "19")
        finally:
            sys.stdin = old_stdin
    
    def test_solve_function_multiple(self):
        """Test main function with multiple test cases"""
        input_data = """2
3 3
0 1 5
1 2 3
0 2 1
4 4
0 1 2
1 2 3
2 3 1
0 3 4"""
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_mst()
            self.assertEqual(len(results), 2)
            self.assertEqual(results[0], "4")
            self.assertEqual(results[1], "6")
        finally:
            sys.stdin = old_stdin
    
    def test_solve_function_disconnected(self):
        """Test main function with disconnected graph"""
        input_data = """1
5 3
0 1 5
1 2 3
3 4 2"""
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_mst()
            self.assertEqual(len(results), 1)
            self.assertEqual(results[0], "Disconnected Graph")
        finally:
            sys.stdin = old_stdin

def run_specific_test():
    """Run specific test cases to verify functionality"""
    print("=== Testing Kruskal's MST Algorithm ===")
    
    # Test 1: Simple connected graph
    print("\n1. Simple Connected Graph:")
    kruskal1 = KruskalMST(4)
    kruskal1.add_edge(0, 1, 10)
    kruskal1.add_edge(0, 2, 6)
    kruskal1.add_edge(0, 3, 5)
    kruskal1.add_edge(1, 3, 15)
    kruskal1.add_edge(2, 3, 4)
    
    result1 = kruskal1.find_mst()
    print(f"Simple graph MST weight: {result1} (expected: 19)")
    
    # Test 2: Disconnected graph
    print("\n2. Disconnected Graph:")
    kruskal2 = KruskalMST(5)
    kruskal2.add_edge(0, 1, 5)
    kruskal2.add_edge(1, 2, 3)
    kruskal2.add_edge(3, 4, 2)
    
    result2 = kruskal2.find_mst()
    print(f"Disconnected graph result: {result2} (expected: Disconnected Graph)")
    
    # Test 3: Complex graph analysis
    print("\n3. Complex Graph Analysis:")
    kruskal3 = KruskalMST(6)
    kruskal3.add_edge(0, 1, 4)
    kruskal3.add_edge(0, 2, 3)
    kruskal3.add_edge(1, 2, 1)
    kruskal3.add_edge(1, 3, 2)
    kruskal3.add_edge(2, 3, 4)
    kruskal3.add_edge(3, 4, 2)
    kruskal3.add_edge(4, 5, 3)
    
    result3 = kruskal3.find_mst()
    print(f"Complex graph MST weight: {result3} (expected: 11)")
    print("MST edges should be: 1-2(1), 1-3(2), 3-4(2), 0-2(3), 4-5(3)")

if __name__ == '__main__':
    # Run specific tests first
    run_specific_test()
    print("\n" + "="*50 + "\n")
    
    # Run unit tests
    unittest.main(verbosity=2)
