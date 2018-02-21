import requests
from decimal import Decimal


def get_price_usd(symbol):
    """
    :type symbol: str
    """
    data = requests.get("https://min-api.cryptocompare.com/data/pricemulti?fsyms=%s&tsyms=USD" % symbol.upper()).json()
    if symbol.upper() in data:
        return Decimal(data[symbol.upper()]['USD'])
    else:
        return Decimal('0')
