from decimal import Decimal, ROUND_DOWN
from typing import Iterable

from monotable.table import MonoTable


def format_usd(price_usd: Decimal) -> Decimal:
    return price_usd.quantize(Decimal('0.01'), rounding=ROUND_DOWN)


def format_curr_balance(b: Decimal, decimal_places) -> Decimal:
    return b.quantize(Decimal(pow(Decimal('1.0'), decimal_places)), rounding=ROUND_DOWN)  # type: ignore


def table(headings: Iterable[str]=(),
          formats: Iterable[str]=(),
          cellgrid: Iterable[Iterable[object]]=((),),
          title: str='',
          ):
    # type: (...) -> str
    """Wrapper to :py:meth:`monotable.table.MonoTable.table`."""
    tbl = MonoTable()
    tbl.guideline_chars = ''
    return tbl.table(headings, formats, cellgrid, title)
