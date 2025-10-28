import unittest
import sys
from io import StringIO
from solution import KosarajuSCC, main

class TestKosarajuSCC(unittest.TestCase):
    
    def test_connected_graph_one_scc(self):
        """Test case where all nodes form one large SCC"""
        input_data = """8 14
0 1
1 2
2 3
2 4
3 0
4 5
5 6
6 4
6 7
7 5
1 5
4 1
5 2
7 7"""
        
        old_stdin = sys.stdin
        old_stdout = sys.stdout
        
        try:
            sys.stdin = StringIO(input_data)
            sys.stdout = StringIO()
            
            result = main()
            
            # Should be ONE SCC containing all nodes
            self.assertEqual(len(result), 1)
            self.assertEqual(set(result[0]), {0, 1, 2, 3, 4, 5, 6, 7})
            
        finally:
            sys.stdin = old_stdin
            sys.stdout = old_stdout
    
    def test_separated_cycles(self):
        """Test case with truly separated SCCs"""
        input_data = """6 6
0 1
1 2
2 0
3 4
4 3
5 5"""
        
        old_stdin = sys.stdin
        old_stdout = sys.stdout
        
        try:
            sys.stdin = StringIO(input_data)
            sys.stdout = StringIO()
            
            result = main()
            
            scc_sets = [set(comp) for comp in result]
            self.assertEqual(len(scc_sets), 3)
            self.assertIn({5}, scc_sets)
            self.assertIn({3, 4}, scc_sets)
            self.assertIn({0, 1, 2}, scc_sets)
            
        finally:
            sys.stdin = old_stdin
            sys.stdout = old_stdout
    
    def test_all_separate_nodes(self):
        """Test case where all nodes are separate SCCs"""
        input_data = """4 0"""
        
        old_stdin = sys.stdin
        old_stdout = sys.stdout
        
        try:
            sys.stdin = StringIO(input_data)
            sys.stdout = StringIO()
            
            result = main()
            
            self.assertEqual(len(result), 4)
            
        finally:
            sys.stdin = old_stdin
            sys.stdout = old_stdout
    
    def test_single_large_cycle(self):
        """Test case with one large cycle (all nodes in one SCC)"""
        input_data = """5 5
0 1
1 2
2 3
3 4
4 0"""
        
        old_stdin = sys.stdin
        old_stdout = sys.stdout
        
        try:
            sys.stdin = StringIO(input_data)
            sys.stdout = StringIO()
            
            result = main()
            
            self.assertEqual(len(result), 1)
            self.assertEqual(set(result[0]), {0, 1, 2, 3, 4})
            
        finally:
            sys.stdin = old_stdin
            sys.stdout = old_stdout
    
    def test_connected_cycles_form_one_scc(self):
        """Test case where connected cycles form one large SCC"""
        input_data = """5 6
0 1
1 2
2 0
2 3
3 4
4 2"""
        
        old_stdin = sys.stdin
        old_stdout = sys.stdout
        
        try:
            sys.stdin = StringIO(input_data)
            sys.stdout = StringIO()
            
            result = main()
            
            self.assertEqual(len(result), 1)
            self.assertEqual(set(result[0]), {0, 1, 2, 3, 4})
            
        finally:
            sys.stdin = old_stdin
            sys.stdout = old_stdout
    
    def test_self_loops_only(self):
        """Test case with only self-loops"""
        input_data = """3 3
0 0
1 1
2 2"""
        
        old_stdin = sys.stdin
        old_stdout = sys.stdout
        
        try:
            sys.stdin = StringIO(input_data)
            sys.stdout = StringIO()
            
            result = main()
            
            self.assertEqual(len(result), 3)
            
        finally:
            sys.stdin = old_stdin
            sys.stdout = old_stdout

if __name__ == '__main__':
    unittest.main()