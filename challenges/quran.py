from more_itertools import ilen

from .challenge import register_challenge

from .utils.quran import get_verse_words
from .utils.caesar import encrypt as caesar


def get_key(word: str, index: int) -> int:
    return ilen(get_verse_words(index + 1, len(word)))


def encrypt(plain: str) -> str:
    """
    A separate Caesar-cipher for each word, based on its index and length, with the Holy Quran as the key.
    The Caesar shift for each word is the number of words in Quran verse <word-index>:<word-length> (surah:verse).
    """
    return " ".join(caesar(word, get_key(word, index)) for index, word in enumerate(plain.split()))


register_challenge(encrypt, "https://quran.com/")
