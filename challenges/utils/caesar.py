from .general import normalize_plain, join_chars

_ALPHABET_START = ord("A")
_ALPHABET_LEN = 26


def _substitute(letter: str, shift: int) -> str:
    return chr((ord(letter) - _ALPHABET_START + shift) % _ALPHABET_LEN + _ALPHABET_START)


@normalize_plain
def encrypt(plain: str, key: int) -> str:
    return join_chars(_substitute(char, key) if char.isalpha() else char for char in plain)
