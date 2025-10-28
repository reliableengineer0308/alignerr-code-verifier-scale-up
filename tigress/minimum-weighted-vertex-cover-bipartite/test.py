import unittest
import sys
from io import StringIO
from solution import solve_bipartite_vertex_cover

class TestBipartiteVertexCover(unittest.TestCase):
    
    def test_simple_case(self):
        input_data = """1
2 2
5 10
3 7
0 0
0 1
1 0
-1 -1"""
        
        expected = [
            "Case #1: 8",
            "L: 0 R: 0"
        ]
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_bipartite_vertex_cover()
            self.assertEqual(results, expected)
        finally:
            sys.stdin = old_stdin
    
    def test_complex_multiple_components(self):
        input_data = """2
3 3
10 20 30
15 25 35
0 0
0 1
1 1
1 2
2 2
-1 -1
2 2
100 200
150 250
0 0
1 1
-1 -1"""
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_bipartite_vertex_cover()
            self.assertEqual(len(results), 4)
            self.assertEqual(results[0], "Case #1: 60") 
            self.assertEqual(results[1], "L: 0,1,2 R: ") 
            self.assertEqual(results[2], "Case #2: 300")
            self.assertEqual(results[3], "L: 0,1 R: ") 
        finally:
            sys.stdin = old_stdin
    
    def test_all_vertices_required(self):
        input_data = """1
3 3
1 1 1
1 1 1
0 0
0 1
0 2
1 0
1 1
1 2
2 0
2 1
2 2
-1 -1"""
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_bipartite_vertex_cover()
            self.assertEqual(len(results), 2)
            self.assertEqual(results[0], "Case #1: 3")
            self.assertTrue(results[1] == "L: 0,1,2 R: " or results[1] == "L:  R: 0,1,2")
        finally:
            sys.stdin = old_stdin
    
    def test_no_edges(self):
        input_data = """1
2 2
1 2
3 4
-1 -1"""
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_bipartite_vertex_cover()
            self.assertEqual(len(results), 2)
            self.assertEqual(results[0], "Case #1: 0")
            self.assertEqual(results[1], "L:  R: ")
        finally:
            sys.stdin = old_stdin
    
    def test_single_edge(self):
        input_data = """1
1 1
5
10
0 0
-1 -1"""
        
        old_stdin = sys.stdin
        sys.stdin = StringIO(input_data)
        
        try:
            results = solve_bipartite_vertex_cover()
            self.assertEqual(len(results), 2)
            self.assertEqual(results[0], "Case #1: 5")
            self.assertEqual(results[1], "L: 0 R: ")
        finally:
            sys.stdin = old_stdin

def run_specific_test():
    test_input = """2
3 3
10 20 30
15 25 35
0 0
0 1
1 1
1 2
2 2
-1 -1
2 2
100 200
150 250
0 0
1 1
-1 -1"""

    old_stdin = sys.stdin
    sys.stdin = StringIO(test_input)
    
    try:
        results = solve_bipartite_vertex_cover()
        print("Results:")
        for result in results:
            print(result)
    finally:
        sys.stdin = old_stdin

if __name__ == '__main__':
    run_specific_test()
    print("\n" + "="*50 + "\n")
    unittest.main(verbosity=2)