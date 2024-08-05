# Refactored Soundex.py

class Soundex:
    def __init__(self):
        self.soundex_mapping = {
            'b': '1', 'f': '1', 'p': '1', 'v': '1',
            'c': '2', 'g': '2', 'j': '2', 'k': '2', 'q': '2', 's': '2', 'x': '2', 'z': '2',
            'd': '3', 't': '3',
            'l': '4',
            'm': '5', 'n': '5',
            'r': '6'
        }
    
    def encode(self, word):
        if not word:
            return ""
        
        word = word.lower()
        soundex_code = word[0].upper()
        previous_digit = ''
        
        for char in word[1:]:
            digit = self._get_digit(char)
            
            if digit == previous_digit:
                continue
            
            soundex_code += digit
            previous_digit = digit
            
            if len(soundex_code) == 4:
                break
        
        return self._pad_soundex_code(soundex_code)
    
    def _get_digit(self, char):
        if char in "aeiouyhw":
            return ''
        return self.soundex_mapping.get(char, '')
    
    def _pad_soundex_code(self, soundex_code):
        return soundex_code.ljust(4, '0')
