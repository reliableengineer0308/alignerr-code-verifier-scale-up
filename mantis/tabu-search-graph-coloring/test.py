import unittest
import sys
from io import StringIO
from solution import solve_graph_coloring, TabuSearchGraphColoring

class TestTabuSearchGraphColoring(unittest.TestCase):
    
    def create_test_graph(self):
        """Create a simple test graph (cycle of 5 vertices)"""
        graph = [[] for _ in range(5)]
        edges = [(0,1), (1,2), (2,3), (3,4), (4,0)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        return graph
    
    def create_bipartite_graph(self):
        """Create a bipartite graph (2-colorable)"""
        graph = [[] for _ in range(6)]
        edges = [(0,3), (0,4), (0,5), (1,3), (1,4), (1,5), (2,3), (2,4), (2,5)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        return graph
    
    def test_graph_construction(self):
        """Test graph construction"""
        graph = self.create_test_graph()
        self.assertEqual(len(graph), 5)
        self.assertEqual(len(graph[0]), 2)  # Vertex 0 connected to 1 and 4
    
    def test_conflict_counting(self):
        """Test conflict counting"""
        graph = self.create_test_graph()
        ts = TabuSearchGraphColoring(graph, 5, 10, 100)
        
        # Valid 3-coloring
        ts.colors = [0, 1, 2, 0, 1]
        ts.num_colors = 3
        conflicts = ts.count_conflicts()
        self.assertEqual(conflicts, 0)
        
        # Invalid coloring with conflict
        ts.colors = [0, 0, 1, 2, 0]  # 0-1 and 4-0 conflicts
        conflicts = ts.count_conflicts()
        self.assertEqual(conflicts, 2)  # Two conflicting edges
    
    def test_valid_coloring_check(self):
        """Test valid coloring check"""
        graph = self.create_test_graph()
        ts = TabuSearchGraphColoring(graph, 5, 10, 100)
        
        # Valid coloring
        ts.colors = [0, 1, 2, 0, 1]
        self.assertTrue(ts.is_valid_coloring())
        
        # Invalid coloring
        ts.colors = [0, 0, 1, 2, 0]
        self.assertFalse(ts.is_valid_coloring())
    
    def test_upper_bound_estimation(self):
        """Test upper bound estimation"""
        graph = self.create_test_graph()
        ts = TabuSearchGraphColoring(graph, 5, 10, 100)
        upper_bound = ts.estimate_upper_bound()
        
        # For a cycle of 5, greedy should use at most 3 colors
        self.assertTrue(2 <= upper_bound <= 3)
    
    def test_small_graph_coloring(self):
        """Test graph coloring with small graph"""
        input_data = """5 5
0 1
1 2
2 3
3 4
4 0
10 100"""
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_graph_coloring()
            self.assertEqual(len(results), 2)
            
            num_colors = int(results[0])
            coloring = list(map(int, results[1].split()))
            
            # Check valid coloring for cycle graph
            self.assertEqual(len(coloring), 5)
            self.assertTrue(2 <= num_colors <= 3)  # Cycle of 5 is 3-colorable
            
            # Verify coloring is valid
            graph = self.create_test_graph()
            for u in range(5):
                for v in graph[u]:
                    self.assertNotEqual(coloring[u], coloring[v])
                    
        finally:
            sys.stdin = old_stdin
    
    def test_bipartite_graph(self):
        """Test 2-colorable (bipartite) graph"""
        input_data = """6 9
0 3
0 4
0 5
1 3
1 4
1 5
2 3
2 4
2 5
10 100"""
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_graph_coloring()
            self.assertEqual(len(results), 2)
            
            num_colors = int(results[0])
            coloring = list(map(int, results[1].split()))
            
            # Bipartite graph should be 2-colorable
            self.assertEqual(num_colors, 2)
            self.assertEqual(len(coloring), 6)
            
        finally:
            sys.stdin = old_stdin

def run_specific_test():
    """Run specific test to verify implementation"""
    test_input = """5 5
0 1
1 2
2 3
3 4
4 0
10 100"""
    
    print("=== Running Tabu Search Graph Coloring Test ===")
    old_stdin = sys.stdin
    sys.stdin = StringIO(test_input)
    
    try:
        results = solve_graph_coloring()
        print("Results:")
        print(f"Colors used: {results[0]}")
        print(f"Coloring: {results[1]}")
    finally:
        sys.stdin = old_stdin

if __name__ == '__main__':
    # Run specific test first
    run_specific_test()
    print("\n" + "="*50 + "\n")
    
    # Run unit tests
    unittest.main(verbosity=2)