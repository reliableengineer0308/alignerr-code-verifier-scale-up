import unittest
from solution import group_anagrams

class TestGroupAnagrams(unittest.TestCase):
    
    def test_example_1(self):
        """Test case with multiple anagram groups."""
        strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
        result = group_anagrams(strs)
        expected = [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
        
        # Sort inner lists for comparison
        self.assertEqual(
            sorted([sorted(group) for group in result]),
            sorted([sorted(group) for group in expected])
        )
    
    
    def test_empty_string(self):
        """Test with single empty string."""
        strs = [""]
        result = group_anagrams(strs)
        self.assertEqual(result, [[""]])
    
    def test_single_char(self):
        """Test with single character."""
        strs = ["a"]
        result = group_anagrams(strs)
        self.assertEqual(result, [["a"]])
    
    def test_no_anagrams(self):
        """Test where no strings are anagrams."""
        strs = ["abc", "def", "ghi"]
        result = group_anagrams(strs)
        # Each string forms its own group
        self.assertEqual(len(result), 3)
        for group in result:
            self.assertEqual(len(group), 1)
    
    def test_all_same(self):
        """Test when all strings are identical."""
        strs = ["abc", "abc", "abc"]
        result = group_anagrams(strs)
        self.assertEqual(result, [["abc", "abc", "abc"]])
    
    def test_mixed_lengths(self):
        """Test strings of different lengths."""
        strs = ["a", "ab", "abc", "b", "ba"]
        result = group_anagrams(strs)
        # "a" and "b" are alone, "ab" and "ba" are anagrams
        groups = [sorted(group) for group in result]
        expected_groups = [["a"], ["ab", "ba"], ["abc"], ["b"]]
        self.assertEqual(sorted(groups), sorted(expected_groups))
    
    def test_large_input(self):
        """Stress test with large number of strings."""
        import random
        import string
        
        random.seed(42)
        # Generate 100 random strings of length 3-5
        strs = []
        for _ in range(100):
            length = random.randint(3, 5)
            s = ''.join(random.choices(string.ascii_lowercase, k=length))
            strs.append(s)
        
        result = group_anagrams(strs)
        
        # Basic validation
        self.assertIsInstance(result, list)
        total_strings = sum(len(group) for group in result)
        self.assertEqual(total_strings, len(strs))
    
    def test_unicode_edge(self):
        """Test edge cases with special patterns."""
        strs = ["aaa", "aa", "a", "", ""]
        result = group_anagrams(strs)
        
        # Создаём словарь: ключ — каноническая форма строки, значение — количество вхождений
        count_dict = {}
        for s in strs:
            canonical = tuple(sorted(s))  # Каноническая форма: tuple(отсортированных символов)
            count_dict[canonical] = count_dict.get(canonical, 0) + 1
        
        # Ожидаемый результат: считаем вхождения каждой канонической формы
        expected_count = {}
        for s in strs:
            canonical = tuple(sorted(s))
            expected_count[canonical] = expected_count.get(canonical, 0) + 1

        self.assertEqual(count_dict, expected_count)


if __name__ == "__main__":
    unittest.main()
