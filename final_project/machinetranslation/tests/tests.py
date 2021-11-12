import unittest

from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    def test_en_to_fr(self):       
        self.assertEqual(english_to_french(''), '')
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertNotEqual(english_to_french('Hello'), 'Bon')

    def test_fr_to_en(self):
        self.assertEqual(french_to_english(''), '')
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertNotEqual(french_to_english('Bon'), 'Hello')

if __name__ == '__main__':
    unittest.main()
    