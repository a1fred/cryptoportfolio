from decimal import Decimal

import requests

from cryptoportfolio.interfaces.base import Address


class F2PoolWallet(Address):
    decimal_places = 18
    symbol = None

    f2pool_currecnices_mapping = {
        'bitcoin': "BTC",
        'litecoin': "LTC",
        'etc': "ETC",
        'eth': "ETH",
        'zec': "ZEC",
        'sc': "SC",
        'monero': "XMR",
        'dash': "DASH",
    }

    def __init__(self, currency, user, **kwargs):
        assert currency in self.f2pool_currecnices_mapping.keys()
        self.symbol = self.f2pool_currecnices_mapping[currency]
        self.currency = currency
        self.user = user
        super(F2PoolWallet, self).__init__(**kwargs)

    def _get_addr_coins_and_tokens_balance(self):
        result = requests.get("http://api.f2pool.com/%s/%s" % (self.currency, self.user)).json()
        return [
            (self.symbol, Decimal(result['balance']))
        ]
