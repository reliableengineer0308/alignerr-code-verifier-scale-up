import unittest
import sys
from io import StringIO
from solution import Dinic, solve_max_flow

class TestMaxFlow(unittest.TestCase):
    
    def test_dinic_basic_flow(self):
        """Test basic flow network"""
        dinic = Dinic(4)
        dinic.add_edge(0, 1, 10)
        dinic.add_edge(0, 2, 10)
        dinic.add_edge(1, 2, 1)
        dinic.add_edge(1, 3, 10)
        dinic.add_edge(2, 3, 10)
        
        max_flow = dinic.max_flow(0, 3)
        self.assertEqual(max_flow, 20)
    
    def test_dinic_complex_network(self):
        """Test complex network from example"""
        dinic = Dinic(6)
        edges = [
            (0, 1, 16), (0, 2, 13), (1, 2, 10),
            (1, 3, 12), (2, 1, 4), (2, 4, 14),
            (3, 2, 9), (3, 5, 20), (4, 3, 7), (4, 5, 4)
        ]
        
        for u, v, cap in edges:
            dinic.add_edge(u, v, cap)
        
        max_flow = dinic.max_flow(0, 5)
        self.assertEqual(max_flow, 23)
    
    def test_no_flow_possible(self):
        """Test case where no flow is possible"""
        dinic = Dinic(3)
        dinic.add_edge(0, 1, 10)
        dinic.add_edge(1, 0, 5)  # Creates cycle but no path to sink
        
        max_flow = dinic.max_flow(0, 2)
        self.assertEqual(max_flow, 0)
    
    def test_direct_edge_only(self):
        """Test single direct edge"""
        dinic = Dinic(2)
        dinic.add_edge(0, 1, 15)
        
        max_flow = dinic.max_flow(0, 1)
        self.assertEqual(max_flow, 15)
    
    def test_flow_values_retrieval(self):
        """Test retrieving flow values for edges"""
        dinic = Dinic(4)
        original_edges = [
            (0, 1, 10), (0, 2, 10), (1, 2, 1), (1, 3, 10), (2, 3, 10)
        ]
        
        for u, v, cap in original_edges:
            dinic.add_edge(u, v, cap)
        
        max_flow = dinic.max_flow(0, 3)
        flows = dinic.get_flows(original_edges)
        
        self.assertEqual(max_flow, 20)
        self.assertEqual(len(flows), 5)
        # Sum of flows from source should equal max flow
        self.assertEqual(flows[0] + flows[1], max_flow)
    
    def test_solve_max_flow_single_case(self):
        """Test main solve function with single test case"""
        input_data = """1
4 5
0 3
0 1 10
0 2 10
1 2 1
1 3 10
2 3 10"""
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_max_flow()
            self.assertEqual(len(results), 2)
            self.assertEqual(results[0], "Case #1: 20")
            # Check that we have 5 flow values
            flow_values = list(map(int, results[1].split()))
            self.assertEqual(len(flow_values), 5)
            self.assertEqual(sum(flow_values[:2]), 20)  # Flow from source
        finally:
            sys.stdin = old_stdin
    
    def test_solve_max_flow_multiple_cases(self):
        """Test main solve function with multiple test cases"""
        input_data = """2
4 4
0 3
0 1 5
1 3 10
0 2 10
2 3 5
3 3
0 2
0 1 8
1 2 12
2 0 3"""
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_max_flow()
            self.assertEqual(len(results), 4)  # 2 cases * 2 lines each
            self.assertEqual(results[0], "Case #1: 10")
            self.assertEqual(results[2], "Case #2: 8")
            
            # Check flow values for first case
            flow_values1 = list(map(int, results[1].split()))
            self.assertEqual(len(flow_values1), 4)
            
            # Check flow values for second case  
            flow_values2 = list(map(int, results[3].split()))
            self.assertEqual(len(flow_values2), 3)
            
        finally:
            sys.stdin = old_stdin
    
    def test_complex_example_from_prompt(self):
        """Test the complex example from prompt"""
        input_data = """1
6 10
0 5
0 1 16
0 2 13
1 2 10
1 3 12
2 1 4
2 4 14
3 2 9
3 5 20
4 3 7
4 5 4"""
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_max_flow()
            self.assertEqual(len(results), 2)
            self.assertEqual(results[0], "Case #1: 23")
            
            flow_values = list(map(int, results[1].split()))
            self.assertEqual(len(flow_values), 10)
            
        finally:
            sys.stdin = old_stdin
    
    def test_zero_capacity_edges(self):
        """Test edges with zero capacity"""
        dinic = Dinic(3)
        dinic.add_edge(0, 1, 0)  # Zero capacity
        dinic.add_edge(1, 2, 10)
        
        max_flow = dinic.max_flow(0, 2)
        self.assertEqual(max_flow, 0)

def run_specific_test():
    """Run specific test cases to verify functionality"""
    print("=== Testing Maximum Flow ===")
    
    # Test case 1: Basic flow
    dinic1 = Dinic(4)
    edges1 = [(0, 1, 10), (0, 2, 10), (1, 2, 1), (1, 3, 10), (2, 3, 10)]
    for u, v, cap in edges1:
        dinic1.add_edge(u, v, cap)
    
    flow1 = dinic1.max_flow(0, 3)
    print(f"Basic flow test: {flow1} (expected: 20)")
    
    # Test case 2: Complex network
    dinic2 = Dinic(6)
    edges2 = [
        (0, 1, 16), (0, 2, 13), (1, 2, 10), (1, 3, 12),
        (2, 1, 4), (2, 4, 14), (3, 2, 9), (3, 5, 20),
        (4, 3, 7), (4, 5, 4)
    ]
    for u, v, cap in edges2:
        dinic2.add_edge(u, v, cap)
    
    flow2 = dinic2.max_flow(0, 5)
    print(f"Complex network test: {flow2} (expected: 23)")

if __name__ == '__main__':
    # Run specific tests first
    run_specific_test()
    print("\n" + "="*50 + "\n")
    
    # Run unit tests
    unittest.main(verbosity=2)