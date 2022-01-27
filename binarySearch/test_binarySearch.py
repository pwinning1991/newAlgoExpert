import binarySearch as program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(program.binarySearch([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 33), 3)