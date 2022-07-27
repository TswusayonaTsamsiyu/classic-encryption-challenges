from itertools import cycle
from more_itertools import take
from string import ascii_uppercase as abc

from .challenge import register_challenge

_TABULA_RECTA = [abc[shift:] + abc[:shift] for shift in range(len(abc))]
_LETTER_INDICES = {letter: index for index, letter in enumerate(abc)}
_KEYWORD = "mango".upper()


def _repeat_keyword(keyword: str, plain: str) -> str:
    return "".join(take(len(plain), cycle(keyword)))


def encrypt_letter(key: str, plain: str) -> str:
    try:
        return _TABULA_RECTA[_LETTER_INDICES[key]][_LETTER_INDICES[plain]]
    except KeyError:
        return plain


def encrypt(plain: str) -> str:
    """
    Implementation of the Vigenère cipher.
    """
    return "".join(encrypt_letter(row, col) for row, col in zip(_repeat_keyword(_KEYWORD, plain), plain.upper()))


register_challenge(encrypt, "https://en.wikipedia.org/wiki/Blaise_de_Vigen%C3%A8re")
