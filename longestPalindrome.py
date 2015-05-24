class LongestPalindrome(object):
	"""Finds the longest palindrome in a string"""
	def __init__(self, string):
		self.string = string
		self.size = len(string)

	def find_longest_palindrome(self):
		if self.size == 0:
			return '', (0, 0)
		elif self.size == 1:
			return self.string, (0, 1)

		odd_radius, best_odd_center = max(self.iter_odd_palindromes_per_center())
		even_radius, best_even_left_center = max(self.iter_even_palindromes_per_left_center())

		odd_size = 2 * odd_radius + 1
		even_size = 2 * even_radius

		if odd_size > even_size:
			left = best_odd_center - odd_radius
			right = best_odd_center + odd_radius
		else:
			left = best_even_left_center - even_radius + 1
			right = best_even_left_center + even_radius

		substring = self.string[left : right+1]
		return substring, (left, right+1)


	# Yields (center, radius_around_center)
	def iter_odd_palindromes_per_center(self):
		for center in xrange(self.size):
			yield self.find_longest_odd_palindrome_at_center(center), center

	# Yields (left_center, radius_around_center**)
	# ** center being in between left_center and right_center
	def iter_even_palindromes_per_left_center(self):
		for left_center in xrange(self.size - 1):
			yield self.find_longest_even_palindrome_at_left_center(left_center), left_center

	def find_longest_odd_palindrome_at_center(self, center):
		elements_to_the_left = center
		elements_to_the_right = self.size - center - 1
		assert elements_to_the_left + 1 + elements_to_the_right == self.size
		max_radius = min(elements_to_the_left, elements_to_the_right)

		best_radius = 0
		for radius in xrange(1, max_radius + 1):
			if self.string[center - radius] == self.string[center + radius]:
				best_radius = radius
			else:
				break

		return best_radius

	def find_longest_even_palindrome_at_left_center(self, left_center):
			elements_to_the_left = left_center + 1
			elements_to_the_right = self.size - left_center - 1
			assert elements_to_the_left + elements_to_the_right == self.size
			max_radius = min(elements_to_the_left, elements_to_the_right)

			best_radius = 0
			for radius in xrange(1, max_radius + 1):
				if self.string[left_center - radius + 1] == self.string[left_center + radius]:
					best_radius = radius
				else:
					break

			return best_radius
