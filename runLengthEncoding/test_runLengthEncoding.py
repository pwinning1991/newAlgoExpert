import runLengthEncoding as program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        string = "AAA"
        expected = "3A"
        actual = program.runLengthEncoding(string)
        self.assertEqual(actual, expected)
    def test_case_2(self):
        string = "AAAAAAAAAAAAABBCCCCDD"
        expected = "9A4A2B4C2D"
        actual = program.runLengthEncoding(string)
        self.assertEqual(actual, expected)