import re
from typing import Iterable


def remove_whitespaces(string: str) -> str:
    return re.sub(r"\s+", "", string)


def join_chars(iterable: Iterable) -> str:
    return "".join(iterable)


def pairs(iterable: Iterable) -> Iterable[tuple]:
    return ((a, b) for a in iterable for b in iterable)
