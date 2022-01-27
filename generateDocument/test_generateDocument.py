from xml.dom.minidom import Document
import generateDocument as program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        characters = ""
        document = "This is a string"
        expected = False
        actual = program.generateDocument(characters, document)
        self.assertEqual(actual, expected)
    def test_case_2(self):
        characters = "Bste!hetsi ogEAxpelrt x "
        document = "AlgoExpert is the Best!"
        expected = True
        actual = program.generateDocument(characters, document)
        self.assertEqual(actual, expected)