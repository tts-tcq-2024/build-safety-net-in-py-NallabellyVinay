def get_soundex_code(c):
    """
    Converts a character to its corresponding Soundex code.
    
    Parameters:
    c (str): The character to convert.
    
    Returns:
    str: The Soundex code for the character.
    """
    c = c.upper()
    mapping = {
        'B': '1', 'F': '1', 'P': '1', 'V': '1',
        'C': '2', 'G': '2', 'J': '2', 'K': '2', 'Q': '2', 'S': '2', 'X': '2', 'Z': '2',
        'D': '3', 'T': '3',
        'L': '4',
        'M': '5', 'N': '5',
        'R': '6'
    }
    return mapping.get(c, '0')  # Default to '0' for non-mapped characters


def generate_soundex(name):
    """
    Generates the Soundex code for a given name.
    
    Parameters:
    name (str): The name to convert.
    
    Returns:
    str: The Soundex code for the name.
    """
    if not name:
        return ""

    # Start with the first letter (capitalized)
    soundex = name[0].upper()
    prev_code = get_soundex_code(soundex)

    # Process remaining characters
    for char in name[1:]:
        code = get_soundex_code(char)
        if len(soundex) < 4 and code != '0' and code != prev_code:
            soundex += code
            prev_code = code

    # Pad with zeros if necessary
    soundex = soundex.ljust(4, '0')

    return soundex


# Test the function
print(generate_soundex("Robert"))  # Output: R163
print(generate_soundex("Rupert"))  # Output: R163
print(generate_soundex("Rubin"))   # Output: R150
