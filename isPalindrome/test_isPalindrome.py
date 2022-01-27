import isPalindrome as program
import unittest


class TestProgram(unittest.TestCase):
    def test_case1(self):
        string = 'abcdcba'
        expected = True
        actual = program.isPalindrome(string)
        self.assertEqual(actual, expected)
    def test_case2(self):
        string = 'abcabc'
        expected = False
        actual = program.isPalindrome(string)
        self.assertEqual(actual, expected)
