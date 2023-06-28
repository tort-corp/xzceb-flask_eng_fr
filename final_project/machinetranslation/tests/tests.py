import unittest
from machinetranslation.translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    """Test cases for translating"""
    def test1(self):
        self.assertEqua(english_to_french("hello"), "bonjour")

    def test2(self):
        self.assertEqual(french_to_english("bonjour"), "hello")

    def test3(self):
        self.assertEqual(english_to_french("sing"), "chanter" )

    def test4(self):
        self.assertEqual(french_to_english("chanter"), "sing")


if __name__ == '__main__':    
  unittest.main(exit=False)










