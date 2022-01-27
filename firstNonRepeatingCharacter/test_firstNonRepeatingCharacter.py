import firstNonRepeatingCharacter as program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = "abcdcaf"
        expected = 1
        actual = program.firstNonRepeatingCharacter(input)
        self.assertEqual(actual, expected)
    def test_case_2(self):
        input = "aaaaaab"
        expected = 6
        actual = program.firstNonRepeatingCharacter(input)
        self.assertEqual(actual, expected)
    def test_case_3(self):
        input = "aaaaaaa"
        expected = -1
        actual = program.firstNonRepeatingCharacter(input)
        self.assertEqual(actual, expected)
    def test_case_4(self):
        input = "abcbaaaa"
        expected = 2
        actual = program.firstNonRepeatingCharacter(input)
        self.assertEqual(actual, expected)