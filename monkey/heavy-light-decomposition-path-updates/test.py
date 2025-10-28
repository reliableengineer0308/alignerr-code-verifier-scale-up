import unittest
from solution import HLD, process_hld_queries

class TestHLD(unittest.TestCase):
    def test_basic_operations(self):
        input_data = """6
1 2
1 3
2 4
2 5
3 6
10 20 30 40 50 60
5
QUERY_PATH 4 6
UPDATE 3 35
QUERY_PATH 4 6
ADD_PATH 1 6 5
QUERY_PATH 4 6"""
        
        results = process_hld_queries(input_data)
        self.assertEqual(results, ["60", "60", "65"])
    
    def test_chain_tree(self):
        input_data = """5
1 2
2 3
3 4
4 5
1 2 3 4 5
4
QUERY_PATH 1 5
UPDATE 3 10
QUERY_PATH 1 5
ADD_PATH 2 4 2"""
        
        results = process_hld_queries(input_data)
        self.assertEqual(results, ["5", "10"])
    
    def test_star_tree(self):
        input_data = """4
1 2
1 3
1 4
5 10 15 20
3
QUERY_PATH 2 4
UPDATE 1 25
QUERY_PATH 2 4"""
        
        results = process_hld_queries(input_data)
        self.assertEqual(results, ["20", "25"])

if __name__ == '__main__':
    unittest.main()