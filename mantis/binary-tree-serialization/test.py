import unittest
from solution import Codec

class TestSerializeDeserializeBinaryTree(unittest.TestCase):
    
    def setUp(self):
        self.codec = Codec()
    
    def test_complex_tree_with_negative_values(self):
        input_data = "10 -5 15 null 7 -20 null null null null 25 30"
        serialized = self.codec.serialize(self.codec.deserialize(input_data))
        self.assertEqual(serialized, input_data)
    
    def test_deep_unbalanced_tree(self):
        input_data = "1 2 null 3 null 4 null 5 null 6 null 7"
        serialized = self.codec.serialize(self.codec.deserialize(input_data))
        self.assertEqual(serialized, input_data)
    
    def test_mixed_null_patterns(self):
        input_data = "1 null 2 3 null null 4 5 6 null 7"
        serialized = self.codec.serialize(self.codec.deserialize(input_data))
        self.assertEqual(serialized, input_data)
    
    def test_multiple_test_cases(self):
        test_cases = [
            "1 2 3 null null 4 5",
            "10 -5 15 null 7 -20 null null null null 25 30",
            "1 null 2 3 null null 4 5 6 null 7"
        ]
        
        for input_data in test_cases:
            with self.subTest(input_data=input_data):
                serialized = self.codec.serialize(self.codec.deserialize(input_data))
                self.assertEqual(serialized, input_data)
    
    def test_empty_tree(self):
        input_data = ""
        serialized = self.codec.serialize(self.codec.deserialize(input_data))
        self.assertEqual(serialized, input_data)
    
    def test_single_node(self):
        input_data = "5"
        serialized = self.codec.serialize(self.codec.deserialize(input_data))
        self.assertEqual(serialized, input_data)
    
    def test_tree_with_only_left_child(self):
        input_data = "1 2 null 3 null 4"
        serialized = self.codec.serialize(self.codec.deserialize(input_data))
        self.assertEqual(serialized, input_data)
    
    def test_tree_with_only_right_child(self):
        input_data = "1 null 2 null 3 null 4"
        serialized = self.codec.serialize(self.codec.deserialize(input_data))
        self.assertEqual(serialized, input_data)
    
    def test_complete_binary_tree(self):
        input_data = "1 2 3 4 5 6 7"
        serialized = self.codec.serialize(self.codec.deserialize(input_data))
        self.assertEqual(serialized, input_data)
    
    def test_tree_with_duplicate_values(self):
        input_data = "1 1 1 null null 1 1"
        serialized = self.codec.serialize(self.codec.deserialize(input_data))
        self.assertEqual(serialized, input_data)
    
    def test_large_value_range(self):
        input_data = "-1000 1000 0 null -500 500"
        serialized = self.codec.serialize(self.codec.deserialize(input_data))
        self.assertEqual(serialized, input_data)
    
    def test_complex_nested_structure(self):
        input_data = "1 2 null 3 4 null null 5 null 6 7 null 8 null 9"
        serialized = self.codec.serialize(self.codec.deserialize(input_data))
        self.assertEqual(serialized, input_data)

    def verify_tree_structure(self, original_data):
        root = self.codec.deserialize(original_data)
        reconstructed_data = self.codec.serialize(root)
        self.assertEqual(reconstructed_data, original_data)

if __name__ == '__main__':
    unittest.main()