from string import ascii_uppercase
from more_itertools import chunked, flatten, unzip

from .challenge import register_challenge

from .utils.general import pairs, join_chars, normalize_plain

_ORDERED_PAIRS = list(map(join_chars, pairs(ascii_uppercase)))
_SHUFFLED_PAIRS = list(flatten(unzip(chunked(_ORDERED_PAIRS, 4))))

_ENCRYPT_MAP = dict(zip(_ORDERED_PAIRS, _SHUFFLED_PAIRS))


@normalize_plain
def encrypt(plain: str) -> str:
    """
    Bigraphic substitution based on generic mapping.
    """
    return join_chars(_ENCRYPT_MAP.get(pair, pair) for pair in map(join_chars, chunked(plain, 2)))


register_challenge(encrypt,
                   "https://thumbs.dreamstime.com/z/initial-two-letters-combination-"
                   "logo-set-creative-variation-style-concept-illustration-160416369.jpg")
