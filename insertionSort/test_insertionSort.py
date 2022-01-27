import insertionSort as program
import unittest

class TestProgam(unittest.TestCase):
    def test_case1(self):
        given = [1,2,3,4]
        expected = [1,2,3,4]
        actual = program.insertionSort(given)
        self.assertEqual(expected, actual)
    def test_case2(self):
        given = [5,4,1,6]
        expected = [1,4,5,6]
        actual = program.insertionSort(given)
        self.assertEqual(expected, actual)
    def test_case_3(self):
        self.assertEqual(program.insertionSort([8, 5, 2, 9, 5, 6, 3]), [2, 3, 5, 5, 6, 8, 9])