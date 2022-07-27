from string import ascii_uppercase
from more_itertools import chunked, flatten, unzip

from .challenge import register_challenge

from .utils.general import pairs, join_chars

_ORDERED_PAIRS = list(map(join_chars, pairs(ascii_uppercase)))
_SHUFFLED_PAIRS = list(flatten(unzip(chunked(_ORDERED_PAIRS, 4))))

_ENCRYPT_MAP = dict(zip(_ORDERED_PAIRS, _SHUFFLED_PAIRS))


def encrypt(plain: str) -> str:
    """
    Bigraphic substitution based on generic mapping.
    """
    pairs = ("".join(pair) for pair in chunked(plain.upper(), 2))
    return "".join(_ENCRYPT_MAP.get(pair, pair) for pair in pairs)


register_challenge(encrypt,
                   "https://thumbs.dreamstime.com/z/initial-two-letters-combination-"
                   "logo-set-creative-variation-style-concept-illustration-160416369.jpg")
