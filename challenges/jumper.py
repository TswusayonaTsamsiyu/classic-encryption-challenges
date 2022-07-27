from more_itertools import interleave_longest

from .challenge import register_challenge

from .utils.general import normalize_plain, join_chars


@normalize_plain
def encrypt(plain: str) -> str:
    """
    Takes the last character, then the first, then the second to last, then the second, ... all the way to the middle.
    """
    half_len = len(plain) // 2
    return join_chars(interleave_longest(reversed(plain[half_len:]), plain[:half_len]))


register_challenge(encrypt, "https://flabfix.com/wp-content/uploads/2019/06/Lateral-Hops-1.gif")
