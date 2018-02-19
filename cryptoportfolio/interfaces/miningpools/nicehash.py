from decimal import Decimal

import requests

from cryptoportfolio.interfaces.base import Address


class NicehashWallet(Address):
    decimal_places = 18

    def __init__(self, id, key, **kwargs):
        self.id = id
        self.key = key
        super(NicehashWallet, self).__init__(**kwargs)

    def _get_addr_coins_and_tokens_balance(self):
        result = requests.get("https://api.nicehash.com/api?method=balance&id=%s&key=%s" % (self.id, self.key)).json()
        return [
            (
                "BTC",
                Decimal(result['result']['balance_confirmed']) + Decimal(result['result']['balance_pending'])
            )
        ]
