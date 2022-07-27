from string import ascii_uppercase
from more_itertools import chunked, flatten

from .challenge import register_challenge

_ORDERED_PAIRS = ["".join((a, b)) for a in ascii_uppercase for b in ascii_uppercase]
_SHUFFLED_PAIRS = list(flatten(zip(*chunked(_ORDERED_PAIRS, 4))))

_ENCRYPT_MAP = {pair: _SHUFFLED_PAIRS[index] for index, pair in enumerate(_ORDERED_PAIRS)}


def encrypt(plain: str) -> str:
    """
    Bigraphic substitution based on generic mapping.
    """
    pairs = ("".join(pair) for pair in chunked(plain.upper(), 2))
    return "".join(_ENCRYPT_MAP.get(pair, pair) for pair in pairs)


register_challenge(encrypt,
                   "https://thumbs.dreamstime.com/z/initial-two-letters-combination-"
                   "logo-set-creative-variation-style-concept-illustration-160416369.jpg")
