import unittest
from solution import min_removals_to_valid

class TestMinRemovalsToValid(unittest.TestCase):

    def test_example_1(self):
        self.assertEqual(min_removals_to_valid("a)bc(d)"), 1)

    def test_example_2(self):
        self.assertEqual(min_removals_to_valid("(a(b)c)"), 0)

    def test_example_3(self):
        self.assertEqual(min_removals_to_valid("))(("), 4)

    def test_example_4(self):
        self.assertEqual(min_removals_to_valid("hello(world)()"), 0)

    def test_example_5(self):
        self.assertEqual(min_removals_to_valid("())(()"), 2)

    def test_empty_string(self):
        self.assertEqual(min_removals_to_valid(""), 0)

    def test_all_letters(self):
        self.assertEqual(min_removals_to_valid("abcdef"), 0)

    def test_only_opening(self):
        self.assertEqual(min_removals_to_valid("((((("), 5)

    def test_only_closing(self):
        self.assertEqual(min_removals_to_valid(")))))"), 5)

    def test_balanced_nested(self):
        self.assertEqual(min_removals_to_valid("((()))"), 0)

    def test_unbalanced_nested(self):
        self.assertEqual(min_removals_to_valid("(((())"), 2)  # one extra '('
        self.assertEqual(min_removals_to_valid("(())))"), 2)  # one extra ')'

    def test_alternating(self):
        """Alternating parentheses: "()()()" → valid; ")()()(" → all mismatched → 4 removals"""
        self.assertEqual(min_removals_to_valid("()()()"), 0)  # balanced
        self.assertEqual(min_removals_to_valid(")()()("), 2)  # mismatched: 4 unmatched parens

    def test_single_parenthesis(self):
        self.assertEqual(min_removals_to_valid("("), 1)
        self.assertEqual(min_removals_to_valid(")"), 1)

    def test_large_input(self):
        # Test with a large valid string (10^4 chars)
        n = 10000
        half = n // 2
        valid_part = '(' * half + ')' * half
        # Insert letters every 10 chars
        large_valid = ''
        for i, c in enumerate(valid_part):
            large_valid += c
            if i % 10 == 0:
                large_valid += 'x'
        self.assertEqual(min_removals_to_valid(large_valid), 0)

    def test_large_unbalanced_opening(self):
        extra_open = '(' * 5000 + ')' * 100
        padded = extra_open + 'a' * (10000 - len(extra_open))
        self.assertEqual(min_removals_to_valid(padded), 4900)  # 5000-100=4900 extra '('

    def test_large_unbalanced_closing(self):
        extra_close = ')' * 3000 + '(' * 200
        padded = extra_close + 'z' * (10000 - len(extra_close))
        self.assertEqual(min_removals_to_valid(padded), 3200)  

    def test_large_alternating_mismatched(self):
        alternating = ''.join(')(' for _ in range(2500))  # 5000 chars
        valid_tail = '()' * 2500  # 5000 more chars
        large_mixed = alternating + valid_tail
        self.assertEqual(min_removals_to_valid(large_mixed), 2)  # first ')' unmatched


    def test_large_all_letters(self):
        all_letters = 'a' * 10000
        self.assertEqual(min_removals_to_valid(all_letters), 0)


    def test_large_nested_valid_with_noise(self):
        depth = 2000
        nested = '(' * depth + ')' * depth
        noisy = ''
        for i, c in enumerate(nested):
            noisy += c
            if i % 50 == 0:
                noisy += 'm'
        noisy += 'x' * (10000 - len(noisy))
        self.assertEqual(min_removals_to_valid(noisy), 0)


    def test_large_edge_case_single_parens(self):
        one_open = '(' + 'a' * 9999
        self.assertEqual(min_removals_to_valid(one_open), 1)

        one_close = 'z' * 9999 + ')'
        self.assertEqual(min_removals_to_valid(one_close), 1)


    def test_large_balanced_with_internal_mismatch(self):
        internal_error = '(' * 3 + ')' * 4 + '('  # "((()))("
        self.assertEqual(min_removals_to_valid(internal_error), 2)  # 1 extra ')', 1 unmatched '('


    def test_performance_stress(self):
        import random
        chars = []
        for _ in range(10000):
            choice = random.randint(0, 2)
            if choice == 0:
                chars.append('(')
            elif choice == 1:
                chars.append(')')
            else:
                chars.append(random.choice('abcdefghijklmnopqrstuvwxyz'))
        test_str = ''.join(chars)
        result = min_removals_to_valid(test_str)
        self.assertIsInstance(result, int)  # Just ensure it runs and returns int




if __name__ == '__main__':
    unittest.main()
