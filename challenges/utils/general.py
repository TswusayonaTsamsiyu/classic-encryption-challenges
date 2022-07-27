import re
from functools import wraps
from typing import Iterable, Callable


def remove_whitespaces(string: str) -> str:
    return re.sub(r"\s+", "", string)


def join_chars(iterable: Iterable[str]) -> str:
    return "".join(iterable)


def join_words(iterable: Iterable[str]) -> str:
    return " ".join(iterable)


def pairs(iterable: Iterable) -> Iterable[tuple]:
    return ((a, b) for a in iterable for b in iterable)


def normalize_plain(encrypt: Callable) -> Callable:
    @wraps(encrypt)
    def wrapper(plain: str, *args) -> str:
        return encrypt(remove_whitespaces(plain.upper()), *args)

    return wrapper
