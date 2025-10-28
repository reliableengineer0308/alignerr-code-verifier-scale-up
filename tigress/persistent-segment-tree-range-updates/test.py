import unittest
from solution import solve_persistent_segment_tree

class TestPersistentSegmentTree(unittest.TestCase):
    
    def test_example1_basic_operations(self):
        input_data = """1
5 10
1 2 3 4 5
QUERY 0 4
UPDATE 1 3 10
QUERY 0 4
CHECKPOINT
UPDATE 2 4 5
QUERY 0 4
ROLLBACK 1
QUERY 0 4
UPDATE 0 0 100
QUERY 0 4"""
        
        expected_output = """Case #1:
15
45
60
45
145"""
        
        output = solve_persistent_segment_tree(input_data)
        self.assertEqual(output, expected_output)
    
    def test_example2_multiple_checkpoints(self):
        input_data = """1
3 8
10 20 30
UPDATE 0 2 5
CHECKPOINT
QUERY 0 2
UPDATE 1 1 10
CHECKPOINT
QUERY 0 2
ROLLBACK 1
QUERY 0 2"""
        
        expected_output = """Case #1:
75
85
75"""
        
        output = solve_persistent_segment_tree(input_data)
        self.assertEqual(output, expected_output)
    
    def test_example3_complex_rollback_scenario(self):
        input_data = """1
4 14
1 1 1 1
UPDATE 0 0 1
CHECKPOINT
UPDATE 1 1 1
CHECKPOINT  
UPDATE 2 2 1
CHECKPOINT
UPDATE 3 3 1
QUERY 0 3
ROLLBACK 2
QUERY 0 3
ROLLBACK 1
QUERY 0 3
ROLLBACK 0
QUERY 0 3"""
        
        expected_output = """Case #1:
8
6
5
4"""
        
        output = solve_persistent_segment_tree(input_data)
        self.assertEqual(output, expected_output)
    
    def test_single_element_array(self):
        input_data = """1
1 8
5
QUERY 0 0
UPDATE 0 0 10
QUERY 0 0
CHECKPOINT
UPDATE 0 0 5
QUERY 0 0
ROLLBACK 1
QUERY 0 0"""
        
        expected_output = """Case #1:
5
15
20
15"""
        
        output = solve_persistent_segment_tree(input_data)
        self.assertEqual(output, expected_output)
    
    def test_multiple_test_cases(self):
        input_data = """2
3 4
1 2 3
QUERY 0 2
UPDATE 0 2 1
QUERY 0 2
CHECKPOINT
2 3
10 20
UPDATE 0 1 5
QUERY 0 1
ROLLBACK 0"""
        
        expected_output = """Case #1:
6
9
Case #2:
40"""
        
        output = solve_persistent_segment_tree(input_data)
        self.assertEqual(output, expected_output)
    
    def test_negative_numbers_and_updates(self):
        input_data = """1
3 8
-5 0 5
QUERY 0 2
UPDATE 0 2 -3
QUERY 0 2
CHECKPOINT
UPDATE 1 1 10
QUERY 0 2
ROLLBACK 1
QUERY 0 2"""
        
        expected_output = """Case #1:
0
-9
1
-9"""
        
        output = solve_persistent_segment_tree(input_data)
        self.assertEqual(output, expected_output)
    
    def test_range_queries_partial_ranges(self):
        input_data = """1
4 9
1 2 3 4
QUERY 0 0
QUERY 1 2
QUERY 3 3
UPDATE 0 3 2
QUERY 0 3
UPDATE 1 2 1
QUERY 0 3
CHECKPOINT
QUERY 1 2"""
        
        expected_output = """Case #1:
1
5
4
18
20
11"""
        
        output = solve_persistent_segment_tree(input_data)
        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()