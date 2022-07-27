from more_itertools import grouper
from typing import Iterable, Reversible

from .challenge import register_challenge

_NUM_COLUMNS = 4
_FILLER = "Z"


def _tabulate(plain: str) -> list[tuple]:
    return list(grouper(plain, _NUM_COLUMNS, fillvalue=_FILLER))


def _boustrophedon(lines: Iterable[Reversible]) -> Iterable[Reversible]:
    return (reversed(column) if index % 2 == 0 else column for index, column in enumerate(lines))


def encrypt(plain: str) -> str:
    """
    Vertical boustrophedon transposition cipher, starting from bottom left corner.
    """
    return "".join("".join(word) for word in _boustrophedon(zip(*_tabulate(plain.upper()))))


register_challenge(encrypt, "https://media.sciencephoto.com/e7/70/12/29/e7701229-800px-wm.jpg")
