import unittest
from solution import merge_k_lists, array_to_list, list_to_array

class TestMergeKLists(unittest.TestCase):
    
    def test_multiple_lists(self):
        lists = [
            array_to_list([1, 4, 5]),
            array_to_list([1, 3, 4]),
            array_to_list([2, 6])
        ]
        result = merge_k_lists(lists)
        self.assertEqual(list_to_array(result), [1, 1, 2, 3, 4, 4, 5, 6])
    
    def test_empty_lists(self):
        lists = []
        result = merge_k_lists(lists)
        self.assertIsNone(result)
    
    def test_single_list(self):
        lists = [array_to_list([1, 2, 3])]
        result = merge_k_lists(lists)
        self.assertEqual(list_to_array(result), [1, 2, 3])
    
    def test_with_empty_list(self):
        lists = [array_to_list([1, 2]), None, array_to_list([3, 4])]
        result = merge_k_lists(lists)
        self.assertEqual(list_to_array(result), [1, 2, 3, 4])
    
    def test_complex_example_4(self):
        lists1 = [
            array_to_list([1, 5, 9, 13, 17, 21]),
            array_to_list([2, 6, 10, 14]),
            array_to_list([3, 7, 11, 15, 19, 23, 27]),
            array_to_list([4, 8, 12, 16, 20])
        ]
        result1 = merge_k_lists(lists1)
        expected1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 19, 20, 21, 23, 27]
        self.assertEqual(list_to_array(result1), expected1)

        lists2 = [
            array_to_list([-5, -3, 0, 2, 8]),
            array_to_list([-4, 1, 7, 9, 12]),
            array_to_list([-2, 4, 6, 10])
        ]
        result2 = merge_k_lists(lists2)
        expected2 = [-5, -4, -3, -2, 0, 1, 2, 4, 6, 7, 8, 9, 10, 12]
        self.assertEqual(list_to_array(result2), expected2)
        
        lists3 = [
            array_to_list([100, 200, 300, 400]),
            array_to_list([50, 150, 250, 350, 450])
        ]
        result3 = merge_k_lists(lists3)
        expected3 = [50, 100, 150, 200, 250, 300, 350, 400, 450]
        self.assertEqual(list_to_array(result3), expected3)
    
    def test_complex_case_1(self):
        lists = [
            array_to_list([1, 5, 9, 13, 17, 21]),
            array_to_list([2, 6, 10, 14]),
            array_to_list([3, 7, 11, 15, 19, 23, 27]),
            array_to_list([4, 8, 12, 16, 20])
        ]
        result = merge_k_lists(lists)
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 19, 20, 21, 23, 27]
        self.assertEqual(list_to_array(result), expected)
    
    def test_complex_case_2(self):
        lists = [
            array_to_list([-5, -3, 0, 2, 8]),
            array_to_list([-4, 1, 7, 9, 12]),
            array_to_list([-2, 4, 6, 10])
        ]
        result = merge_k_lists(lists)
        expected = [-5, -4, -3, -2, 0, 1, 2, 4, 6, 7, 8, 9, 10, 12]
        self.assertEqual(list_to_array(result), expected)
    
    def test_complex_case_3(self):
        lists = [
            array_to_list([100, 200, 300, 400]),
            array_to_list([50, 150, 250, 350, 450])
        ]
        result = merge_k_lists(lists)
        expected = [50, 100, 150, 200, 250, 300, 350, 400, 450]
        self.assertEqual(list_to_array(result), expected)
    
    def test_complex_case_4(self):
        lists = [
            array_to_list([1, 10, 20]),
            array_to_list([2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15]),
            array_to_list([16, 17, 18, 19])
        ]
        result = merge_k_lists(lists)
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        self.assertEqual(list_to_array(result), expected)
    
    def test_complex_case_5(self):
        lists = [
            array_to_list([1, 4, 7, 10]),
            array_to_list([2, 5, 8, 11]),
            array_to_list([3, 6, 9, 12])
        ]
        result = merge_k_lists(lists)
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        self.assertEqual(list_to_array(result), expected)
    
    def test_edge_case_large_gaps(self):
        lists = [
            array_to_list([1, 100, 200]),
            array_to_list([50, 150, 250]),
            array_to_list([25, 75, 125, 175, 225])
        ]
        result = merge_k_lists(lists)
        expected = [1, 25, 50, 75, 100, 125, 150, 175, 200, 225, 250]
        self.assertEqual(list_to_array(result), expected)

    def test_mixed_empty_and_non_empty(self):
        lists = [
            None,
            array_to_list([1, 3, 5]),
            None,
            array_to_list([2, 4, 6]),
            None
        ]
        result = merge_k_lists(lists)
        self.assertEqual(list_to_array(result), [1, 2, 3, 4, 5, 6])

if __name__ == '__main__':
    unittest.main()