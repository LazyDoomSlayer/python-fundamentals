import string
from enum import Enum


class CharacterSet(Enum):
    DIGITS = ("Digits (0-9)", string.digits)
    LOWERCASE = ("Lowercase Letters (a-z)", string.ascii_lowercase)
    UPPERCASE = ("Uppercase Letters (A-Z)", string.ascii_uppercase)
    ASCII = ("ASCII Letters (a-z, A-Z)", string.ascii_letters)
    HEXDIGITS = ("Hex Digits (0-9, a-f)", string.hexdigits)
    WHITESPACE = ("Whitespace", string.whitespace)
    PUNCTUATION = ("Punctuation", string.punctuation)
    CUSTOM = ("Custom Character Set", None)

    @staticmethod
    def get_by_name(name: str):
        for charset in CharacterSet:
            if charset.value[0] == name:
                return charset
        return None
