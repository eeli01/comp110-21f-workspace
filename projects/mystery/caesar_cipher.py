def decode_char(letter: str) -> str:
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
    decoded_word: str = ""
    for index in range(len(word)):
        decoded_word += decode_char(word[index])
    return decoded_word