import unittest
from longestPalindrome import LongestPalindrome

def triplets(iterable):
	it = iter(iterable)

	while True:
		first = next(it)
		try:
			second = next(it)
			third = next(it)
		except StopIteration:
			raise ValueError('Iterable is not a multiple of three')

		yield first, second, third


class LongestPalindromeTest(unittest.TestCase):
	def test_empty_string(self):
		self.assertLongestPalindromeIs('', '', 0, 0)

	def test_singleton(self):
		self.assertLongestPalindromeIs('x', 'x', 0, 1)

	def test_two_different_characters(self):
		self.assertLongestPalindromeIsOneOf('ab',
			'a', 0, 1,
			'b', 1, 2)

	def test_two_same_characters(self):
		self.assertLongestPalindromeIs('aa', 'aa', 0, 2)

	def test_three_same_characters(self):
		self.assertLongestPalindromeIs('aaa', 'aaa', 0, 3)

	def test_non_overlapping_palindromes_same_size(self):
		self.assertLongestPalindromeIsOneOf('aaxybbc',
			'aa', 0, 2,
			'bb', 4, 6)

	def test_non_overlapping_palindromes_different_size(self):
		self.assertLongestPalindromeIs('aaaxybbc', 'aaa', 0, 3)
		self.assertLongestPalindromeIs('aaxybbbc', 'bbb', 4, 7)

	def test_overlapping_palindromes(self):
		self.assertLongestPalindromeIsOneOf('ababab',
			'ababa', 0, 5,
			'babab', 1, 6)
		self.assertLongestPalindromeIs('babcbabcbaccba', 'abcbabcba', 1, 10)

	def assertLongestPalindromeIs(self, text, palindrome, begin, end):
		actual = actual_palindrome, (actual_begin, actual_end) = LongestPalindrome(text).find_longest_palindrome()
		expected = palindrome, (begin, end)
		self.assertEquals(actual, expected)

	def assertLongestPalindromeIsOneOf(self, text, *args):
		actual = actual_palindrome, (actual_begin, actual_end) = LongestPalindrome(text).find_longest_palindrome()
		expected = [ (palindrome, (begin, end)) for palindrome, begin, end in triplets(args) ]
		self.assertIn(actual, expected)
