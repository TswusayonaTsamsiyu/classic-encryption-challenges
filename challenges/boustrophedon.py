from typing import Iterable
from more_itertools import grouper, unzip

from .challenge import register_challenge

from .utils.general import join_chars

_NUM_COLUMNS = 4
_FILLER = "Z"


def _tabulate(plain: str) -> list[tuple]:
    return list(grouper(plain, _NUM_COLUMNS, fillvalue=_FILLER))


def _boustrophedon(lines: Iterable) -> Iterable:
    return (reversed(column) if index % 2 == 0 else column for index, column in enumerate(lines))


def encrypt(plain: str) -> str:
    """
    Vertical boustrophedon transposition cipher, starting from bottom left corner.
    """
    return "".join(map(join_chars, _boustrophedon(unzip(_tabulate(plain.upper())))))


register_challenge(encrypt, "https://media.sciencephoto.com/e7/70/12/29/e7701229-800px-wm.jpg")
