# Enhanced Soundex.test.py
import unittest
from Soundex import Soundex

class TestSoundex(unittest.TestCase):
    def setUp(self):
        self.soundex = Soundex()
    
    def test_empty_string(self):
        self.assertEqual(self.soundex.encode(""), "")
    
    def test_single_letter(self):
        self.assertEqual(self.soundex.encode("A"), "A000")
        self.assertEqual(self.soundex.encode("B"), "B000")
    
    def test_ignore_vowels_and_specific_letters(self):
        self.assertEqual(self.soundex.encode("Ab"), "A100")
        self.assertEqual(self.soundex.encode("Ac"), "A200")
        self.assertEqual(self.soundex.encode("Ad"), "A300")
    
    def test_same_digit_letters(self):
        self.assertEqual(self.soundex.encode("Bb"), "B000")
        self.assertEqual(self.soundex.encode("Cc"), "C000")
        self.assertEqual(self.soundex.encode("Gg"), "G000")
    
    def test_different_digit_letters(self):
        self.assertEqual(self.soundex.encode("Abcd"), "A123")
        self.assertEqual(self.soundex.encode("Abcf"), "A121")
    
    def test_padding(self):
        self.assertEqual(self.soundex.encode("A"), "A000")
        self.assertEqual(self.soundex.encode("Ab"), "A100")
        self.assertEqual(self.soundex.encode("Abc"), "A200")
        self.assertEqual(self.soundex.encode("Abcd"), "A123")
    
    def test_real_words(self):
        self.assertEqual(self.soundex.encode("Ashcraft"), "A261")
        self.assertEqual(self.soundex.encode("Robert"), "R163")
        self.assertEqual(self.soundex.encode("Rupert"), "R163")
        self.assertEqual(self.soundex.encode("Rubin"), "R150")
    
    def test_ignore_case(self):
        self.assertEqual(self.soundex.encode("ashcraft"), "A261")
        self.assertEqual(self.soundex.encode("ASHCRAFT"), "A261")
        self.assertEqual(self.soundex.encode("AshCraft"), "A261")
    
    def test_h_w_separation(self):
        self.assertEqual(self.soundex.encode("Ashcroft"), "A226")
        self.assertEqual(self.soundex.encode("Ashwcroft"), "A226")
    
    def test_vowel_separation(self):
        self.assertEqual(self.soundex.encode("Acht"), "A230")
        self.assertEqual(self.soundex.encode("Aechtt"), "A230")

if __name__ == '__main__':
    unittest.main()
