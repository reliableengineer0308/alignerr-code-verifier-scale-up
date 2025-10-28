import unittest
import sys
from io import StringIO
from solution import main, find_maximum_matching, is_valid_matching

class TestBipartiteMatching(unittest.TestCase):
    
    def run_test_case(self, input_data, expected_matching_size, expected_pairs):

        old_stdin = sys.stdin
        old_stdout = sys.stdout
        
        try:
            sys.stdin = StringIO(input_data)
            sys.stdout = StringIO()
            
            result = main()
            
            output = sys.stdout.getvalue().strip()
            
            # Parse input to get graph information
            lines = input_data.strip().split('\n')
            U, V, E = map(int, lines[0].split())
            edges = []
            for i in range(1, 1 + E):
                u, v = map(int, lines[i].split())
                edges.append((u, v))
            
            # Check if the expected pairs form a valid maximum matching
            is_valid = is_valid_matching(U, V, edges, expected_pairs)
            self.assertTrue(is_valid, 
                          f"Expected matching {expected_pairs} is not a valid maximum matching")
            
            # Check if algorithm found correct size
            self.assertIn(f"Maximum matching: {expected_matching_size}", output)
            
            # Check if algorithm's result is also valid
            if result:
                result_valid = is_valid_matching(U, V, edges, result)
                self.assertTrue(result_valid, 
                              f"Algorithm result {result} is not a valid maximum matching")
            
        finally:
            sys.stdin = old_stdin
            sys.stdout = old_stdout
    
    def test_sample_case(self):

        input_data = """4 4 6
0 1
0 2
1 0
1 3
2 2
3 2"""
        
        expected_pairs = [(0,1), (1,3), (2,2)]
        self.run_test_case(input_data, 3, expected_pairs)
    
    def test_sample_case_alternative(self):
        input_data = """4 4 6
0 1
0 2
1 0
1 3
2 2
3 2"""
        
        expected_pairs = [(0,1), (1,0), (2,2)]
        self.run_test_case(input_data, 3, expected_pairs)
    
    def test_no_edges(self):
        """Test case with no edges"""
        input_data = """3 3 0"""
        expected_pairs = []
        self.run_test_case(input_data, 0, expected_pairs)
    
    def test_perfect_matching(self):
        """Test case with perfect matching"""
        input_data = """3 3 5
0 0
0 1
1 1
1 2
2 2"""
        
        expected_pairs = [(0,0), (1,1), (2,2)]
        self.run_test_case(input_data, 3, expected_pairs)
    
    def test_partial_matching(self):
        """Test case with partial matching"""
        input_data = """4 3 4
0 0
1 0
2 1
3 2"""
        
        expected_pairs = [(0,0), (2,1), (3,2)]
        self.run_test_case(input_data, 3, expected_pairs)
    
    def test_bottleneck_matching(self):
        """Test case with bottleneck (all edges to one node)"""
        input_data = """5 4 5
0 0
1 0
2 0
3 0
4 0"""
        
        expected_pairs = [(0,0)]
        self.run_test_case(input_data, 1, expected_pairs)
    
    def test_asymmetric_matching(self):
        """Test asymmetric case"""
        input_data = """3 5 6
0 0
0 1
1 2
1 3
2 3
2 4"""
        
        expected_pairs = [(0,1), (1,2), (2,4)]
        self.run_test_case(input_data, 3, expected_pairs)
    
    def test_direct_validation(self):
        """Test validation function directly"""
        U, V = 3, 3
        edges = [(0,0), (0,1), (1,1), (1,2), (2,2)]
        
        # Valid maximum matching
        valid_matching = [(0,0), (1,1), (2,2)]
        self.assertTrue(is_valid_matching(U, V, edges, valid_matching))
        
        # Invalid matching (non-existent edge)
        invalid_matching1 = [(0,1), (1,2), (2,0)]
        self.assertFalse(is_valid_matching(U, V, edges, invalid_matching1))
        
        # Invalid matching (duplicate node)
        invalid_matching2 = [(0,1), (1,2), (1,0)]
        self.assertFalse(is_valid_matching(U, V, edges, invalid_matching2))
        
        # Invalid matching (not maximum)
        invalid_matching3 = [(0,1)]
        self.assertFalse(is_valid_matching(U, V, edges, invalid_matching3))

if __name__ == '__main__':
    unittest.main()