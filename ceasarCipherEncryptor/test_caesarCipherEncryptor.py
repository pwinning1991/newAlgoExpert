import caesarCipherEncryptor as program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(program.caesarCipherEncryptor("xyz", 2), "zab")