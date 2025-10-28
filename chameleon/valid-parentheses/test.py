import unittest
from solution import is_valid

class TestValidParentheses(unittest.TestCase):
    
    def test_simple_pairs(self):
        """Test basic valid pairs."""
        self.assertTrue(is_valid("()"))
        self.assertTrue(is_valid("{}"))
        self.assertTrue(is_valid("[]"))
    
    def test_nested_valid(self):
        """Test nested valid parentheses."""
        self.assertTrue(is_valid("([{}])"))
        self.assertTrue(is_valid("{[()]}"))
        self.assertTrue(is_valid("((()))"))
    
    def test_invalid_closing(self):
        """Test wrong closing bracket type."""
        self.assertFalse(is_valid("(]"))
        self.assertFalse(is_valid("[)"))
        self.assertFalse(is_valid("{]"))
    
    def test_wrong_order(self):
        """Test correct types but wrong order."""
        self.assertFalse(is_valid("([)]"))
        self.assertFalse(is_valid("({[)]}"))
    
    
    def test_unbalanced(self):
        """Test unbalanced parentheses."""
        self.assertFalse(is_valid("((("))
        self.assertFalse(is_valid(")))"))
        self.assertFalse(is_valid("{{{}"))
    
    
    def test_empty_string(self):
        """Test empty string (edge case)."""
        self.assertTrue(is_valid(""))
    
    def test_long_valid(self):
        """Stress test with long valid string."""
        s = "()" * 1000 + "[]" * 500 + "{}" * 250
        self.assertTrue(is_valid(s))

if __name__ == "__main__":
    unittest.main()
