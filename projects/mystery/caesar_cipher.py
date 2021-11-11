"""Decoding the note left by Kaki."""

__author__ = "730319741"


def decode_char(letter: str) -> str:
    """Decode just a single character."""
    character: str = ""
    ascii_code: int = ord(letter)
    if letter == "A":
        normalized: int = ascii_code - 65
        encoded_code: int = (normalized - 1) % 26 + 65
        character = chr(encoded_code)
    else: 
        character = chr(ascii_code - 1)
    return character
    

def decode_str(word: str) -> str:
    """Decode a string of characters up to 5."""
    decoded_word: str = ""
    for index in range(len(word)):
        decoded_word += decode_char(word[index])
    return decoded_word


def decode_any_char(letter: str) -> str:
    """Decode any single character."""
    character: str = ""
    ascii_code: int = ord(letter)
    if letter.isalpha() is not True: 
        character = letter
    else: 
        if letter == "A":
            normalized: int = ascii_code - 65
            encoded_code: int = (normalized - 1) % 26 + 65
            character = chr(encoded_code)
        else: 
            if letter == "a":
                normalized = ascii_code - 97
                encoded_code = (normalized - 1) % 26 + 97
                character = chr(encoded_code)       
            else: 
                character = chr(ascii_code - 1)
    return character


def decode_char_by_shift(letter: str, shift: int) -> str:
    # character: str = ""
    # ascii_code: int = ord(letter)
    # if letter.isalpha() is not True: 
    #     character = letter
    # else: 
    #     if letter == "A":
    #         normalized: int = ascii_code - 65
    #         encoded_code: int = (normalized - shift) % 26 + 65
    #         character = chr(encoded_code)
    #     else: 
    #         if letter == "a":
    #             normalized = ascii_code - 97
    #             encoded_code = (normalized - shift) % 26 + 97
    #             character = chr(encoded_code)       
    #         else: 
    #             character = chr(ascii_code - shift)
    # return character


def decode_str_by_shift(word: str, shift: int) -> str:
    decoded_word: str = ""
    i: int = 0
    while i < len(word):
        shifted_letter: str = decode_char_by_shift(word[i], shift) 
        decoded_word += shifted_letter
        i += 1
    return decoded_word