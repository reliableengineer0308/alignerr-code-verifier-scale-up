import unittest
from solution import decode_string

class TestStringDecoding(unittest.TestCase):
    
    def test_nested_encoding(self):
        self.assertEqual(decode_string("3[a2[c]]"), "accaccacc")
    
    def test_multiple_encodings(self):
        self.assertEqual(decode_string("2[abc]3[cd]ef"), "abcabccdcdcdef")
    
    def test_simple_case(self):
        self.assertEqual(decode_string("3[a]2[bc]"), "aaabcbc")
    
    def test_no_encoding(self):
        self.assertEqual(decode_string("abc"), "abc")
    
    def test_single_repetition(self):
        self.assertEqual(decode_string("10[a]"), "a" * 10)
    
    def test_empty_string(self):
        self.assertEqual(decode_string(""), "")

if __name__ == '__main__':
    unittest.main()