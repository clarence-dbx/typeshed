# Stubs for lib2to3.pgen2.tokenize (Python 3.6)
# NOTE: Only elements from __all__ are present.

from typing import Callable, Iterable, Iterator, List, Tuple
from lib2to3.pgen2.token import *  # noqa


_Coord = Tuple[int, int]
_TokenEater = Callable[[int, str, _Coord, _Coord, str], None]
_TokenInfo = Tuple[int, str, _Coord, _Coord, str]


class TokenError(Exception): ...
class StopTokenizing(Exception): ...

def tokenize(readline, tokeneater: _TokenEater = ...) -> None: ...

class Untokenizer:
    tokens: List[str]
    prev_row: int
    prev_col: int
    def __init__(self) -> None: ...
    def add_whitespace(self, start: _Coord): ...
    def untokenize(self, iterable: Iterable[_TokenInfo]) -> str: ...
    def compat(self, token: Tuple[int, str], iterable: Iterable[_TokenInfo]) -> None: ...

def untokenize(iterable: Iterable[_TokenInfo]) -> str: ...
def generate_tokens(
    readline: Callable[[], str]
) -> Iterator[_TokenInfo]: ...
