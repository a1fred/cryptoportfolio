from decimal import Decimal, ROUND_UP


def format_usd(price_usd: Decimal) -> Decimal:
    return price_usd.quantize(Decimal('0.01'), rounding=ROUND_UP)


def format_curr_balance(b: Decimal, decimal_places) -> Decimal:
    return b.quantize(pow(Decimal('1.0'), decimal_places), rounding=ROUND_UP)
