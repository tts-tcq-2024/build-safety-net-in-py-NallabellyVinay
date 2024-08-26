# Soundex.test.py

import unittest
from Soundex import generate_soundex

class TestSoundex(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(generate_soundex(""), "0000")

    def test_single_character(self):
        self.assertEqual(generate_soundex("A"), "A000")

    def test_common_names(self):
        self.assertEqual(generate_soundex("Smith"), "S530")
        self.assertEqual(generate_soundex("Smyth"), "S530")

    def test_similar_sounding_names(self):
        self.assertEqual(generate_soundex("Jackson"), "J025")
        self.assertEqual(generate_soundex("Jaxon"), "J025")

    def test_names_with_special_characters(self):
        self.assertEqual(generate_soundex("O'Connor"), "O252")
        self.assertEqual(generate_soundex("Anne-Marie"), "A052")

    def test_names_with_numbers(self):
        self.assertEqual(generate_soundex("123"), "0000")
        self.assertEqual(generate_soundex("John123"), "J053")

    def test_long_name(self):
        self.assertEqual(generate_soundex("Christopher"), "C362")

    def test_names_with_repeated_letters(self):
        self.assertEqual(generate_soundex("Bobby"), "B010")

    def test_names_with_h_and_w(self):
        self.assertEqual(generate_soundex("Hugh"), "H020")
        self.assertEqual(generate_soundex("Hawkins"), "H252")

if __name__ == '__main__':
    unittest.main()
