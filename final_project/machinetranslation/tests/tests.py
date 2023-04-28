import unittest
import sys

sys.path.insert(1, '/home/project/xzceb-flask_eng_fr/final_project/machinetranslation')
from translator import frenchToEnglish, englishToFrench

class TestTranslator(unittest.TestCase):
    def test_frenchToEnglish_null_input(self):
        self.assertIsNone(frenchToEnglish(None))

    def test_englishToFrench_null_input(self):
        self.assertIsNone(englishToFrench(None))

    def test_frenchToEnglish_hello(self):
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")

    def test_englishToFrench_hello(self):
        self.assertEqual(englishToFrench("Hello"), "Bonjour")

if __name__ == '__main__':
    unittest.main()
