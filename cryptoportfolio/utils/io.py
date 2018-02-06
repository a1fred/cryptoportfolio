from decimal import Decimal, ROUND_UP

from monotable.table import MonoTable


def format_usd(price_usd: Decimal) -> Decimal:
    return price_usd.quantize(Decimal('0.01'), rounding=ROUND_UP)


def format_curr_balance(b: Decimal, decimal_places) -> Decimal:
    return b.quantize(pow(Decimal('1.0'), decimal_places), rounding=ROUND_UP)


def table(headings=(),       # type: Iterable[str]
          formats=(),        # type: Iterable[str]
          cellgrid=((),),    # type: Iterable[Iterable[object]]
          title='',          # type: str
          ):
    # type: (...) -> str
    """Wrapper to :py:meth:`monotable.table.MonoTable.table`."""
    tbl = MonoTable()
    tbl.guideline_chars = ''
    return tbl.table(headings, formats, cellgrid, title)
