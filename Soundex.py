# Soundex.py

def get_soundex_code(c):
    c = c.upper()
    mapping = {
        'B': '1', 'F': '1', 'P': '1', 'V': '1',
        'C': '2', 'G': '2', 'J': '2', 'K': '2', 'Q': '2', 'S': '2', 'X': '2', 'Z': '2',
        'D': '3', 'T': '3',
        'L': '4',
        'M': '5', 'N': '5',
        'R': '6'
    }
    return mapping.get(c, '')

def generate_soundex(name):
    if not name:
        return "0000"
    
    name = name.upper()
    soundex = [name[0]]
    prev_code = get_soundex_code(name[0])

    for char in name[1:]:
        code = get_soundex_code(char)
        if code and code != prev_code:
            soundex.append(code)
            prev_code = code
        if len(soundex) == 4:
            break

    return ''.join(soundex).ljust(4, '0')
