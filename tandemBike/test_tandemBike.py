import tandemBike as program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        redShirtSpeeds = [5, 5, 3, 9, 2]
        blueShirtSpeeds = [3, 6, 7, 2, 1]
        fastest = True
        expected = 32
        actual = program.tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest)
        self.assertEqual(actual, expected)

    def test_case_2(self):
        redShirtSpeeds = [5, 5, 3, 9, 2]
        blueShirtSpeeds = [3, 6, 7, 2, 1]
        fastest = False
        expected = 25 
        actual = program.tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest)
        self.assertEqual(actual, expected)