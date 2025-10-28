import unittest
import sys
from io import StringIO
from solution import HopcroftKarp, solve_bipartite_matching

class TestBipartiteMatching(unittest.TestCase):
    
    def test_basic_bipartite(self):
        """Test basic bipartite graph"""
        hk = HopcroftKarp(3, 3)
        edges = [(1, 1), (1, 2), (2, 2), (2, 3), (3, 1)]
        for u, v in edges:
            hk.add_edge(u, v)
        
        matching = hk.max_matching()
        self.assertEqual(matching, 3)
    
    def test_unbalanced_graph(self):
        """Test unbalanced bipartite graph"""
        hk = HopcroftKarp(4, 3)
        edges = [(1, 1), (1, 2), (2, 1), (2, 3), (3, 2), (4, 3)]
        for u, v in edges:
            hk.add_edge(u, v)
        
        matching = hk.max_matching()
        self.assertEqual(matching, 3)
    
    def test_no_edges(self):
        """Test graph with no edges"""
        hk = HopcroftKarp(2, 2)
        matching = hk.max_matching()
        self.assertEqual(matching, 0)
    
    def test_complete_bipartite(self):
        """Test complete bipartite graph"""
        hk = HopcroftKarp(3, 3)
        for u in range(1, 4):
            for v in range(1, 4):
                hk.add_edge(u, v)
        
        matching = hk.max_matching()
        self.assertEqual(matching, 3)
    
    def test_complex_case_1(self):
        hk = HopcroftKarp(4, 4)
        edges = [(1, 1), (1, 2), (2, 3), (3, 2), (3, 4), (4, 3)]
        for u, v in edges:
            hk.add_edge(u, v)
        
        matching = hk.max_matching()
        self.assertEqual(matching, 3) 
    
    def test_complex_case_2(self):
        hk = HopcroftKarp(5, 5)
        edges = [(1, 1), (1, 2), (2, 2), (2, 3), (3, 3), (3, 4), (4, 4), (4, 5)]
        for u, v in edges:
            hk.add_edge(u, v)
        
        matching = hk.max_matching()
        self.assertEqual(matching, 4)
    
    def test_single_edge(self):
        """Test graph with single edge"""
        hk = HopcroftKarp(1, 1)
        hk.add_edge(1, 1)
        matching = hk.max_matching()
        self.assertEqual(matching, 1)
    
    def test_disconnected_components(self):
        """Test graph with disconnected components"""
        hk = HopcroftKarp(3, 3)
        edges = [(1, 1), (2, 2), (3, 3)]  # Three disconnected edges
        for u, v in edges:
            hk.add_edge(u, v)
        
        matching = hk.max_matching()
        self.assertEqual(matching, 3)
    
    def test_perfect_matching_larger(self):
        """Test case with perfect matching"""
        hk = HopcroftKarp(4, 4)
        edges = [(1, 1), (1, 2), (2, 2), (2, 3), (3, 3), (3, 4), (4, 1), (4, 4)]
        for u, v in edges:
            hk.add_edge(u, v)
        
        matching = hk.max_matching()
        # This graph has perfect matching: 1-2, 2-3, 3-4, 4-1
        self.assertEqual(matching, 4)
    
    def test_solve_function_single(self):
        """Test main function with single test case"""
        input_data = """1
3 3 5
1 1
1 2
2 2
2 3
3 1"""
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_bipartite_matching()
            self.assertEqual(len(results), 1)
            self.assertEqual(results[0], "3")
        finally:
            sys.stdin = old_stdin
    
    def test_solve_function_multiple(self):
        """Test main function with multiple test cases"""
        input_data = """2
4 4 6
1 1
1 2
2 3
3 2
3 4
4 3
5 5 8
1 1
1 2
2 2
2 3
3 3
3 4
4 4
4 5"""
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_bipartite_matching()
            self.assertEqual(len(results), 2)
            self.assertEqual(results[0], "3")
            self.assertEqual(results[1], "4") 
        finally:
            sys.stdin = old_stdin

def run_specific_test():
    """Run specific test cases to verify functionality"""
    print("=== Testing Hopcroft-Karp Bipartite Matching ===")
    
    # Test 1: Basic bipartite graph
    print("\n1. Basic Bipartite Graph:")
    hk1 = HopcroftKarp(3, 3)
    edges1 = [(1, 1), (1, 2), (2, 2), (2, 3), (3, 1)]
    for u, v in edges1:
        hk1.add_edge(u, v)
    
    result1 = hk1.max_matching()
    print(f"Basic graph matching: {result1} (expected: 3)")
    
    # Test 2: Complex case 1 with analysis
    print("\n2. Complex Case 1 Analysis:")
    hk2 = HopcroftKarp(4, 4)
    edges2 = [(1, 1), (1, 2), (2, 3), (3, 2), (3, 4), (4, 3)]
    for u, v in edges2:
        hk2.add_edge(u, v)
    
    result2 = hk2.max_matching()
    print(f"Complex case 1 matching: {result2}")
    print("Graph analysis:")
    print("U1: [V1, V2]")
    print("U2: [V3]") 
    print("U3: [V2, V4]")
    print("U4: [V3]")
    print("Maximum matching should be 3 (not 4)")
    
    # Test 3: Complex case 2 with analysis
    print("\n3. Complex Case 2 Analysis:")
    hk3 = HopcroftKarp(5, 5)
    edges3 = [(1, 1), (1, 2), (2, 2), (2, 3), (3, 3), (3, 4), (4, 4), (4, 5)]
    for u, v in edges3:
        hk3.add_edge(u, v)
    
    result3 = hk3.max_matching()
    print(f"Complex case 2 matching: {result3}")
    print("Graph analysis:")
    print("U1: [V1, V2]")
    print("U2: [V2, V3]")
    print("U3: [V3, V4]")
    print("U4: [V4, V5]")
    print("U5: []")
    print("Maximum matching should be 4 (not 5)")
    
    # Test 4: Perfect matching case
    print("\n4. Perfect Matching Case:")
    hk4 = HopcroftKarp(4, 4)
    edges4 = [(1, 1), (1, 2), (2, 2), (2, 3), (3, 3), (3, 4), (4, 1), (4, 4)]
    for u, v in edges4:
        hk4.add_edge(u, v)
    
    result4 = hk4.max_matching()
    print(f"Perfect matching case: {result4} (expected: 4)")

if __name__ == '__main__':
    # Run specific tests first
    run_specific_test()
    print("\n" + "="*50 + "\n")
    
    # Run unit tests
    unittest.main(verbosity=2)