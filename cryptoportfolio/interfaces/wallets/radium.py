from decimal import Decimal

import requests

from cryptoportfolio.interfaces.base import CryptoCoinWallet


class RadiumWallet(CryptoCoinWallet):
    decimal_places = 18

    def _get_addr_coins_and_tokens_balance(self):
        balance = requests.get(
            "https://chainz.cryptoid.info/rads/api.dws?q=getbalance&a=%s" % self.addr
        ).text
        return [
            ("RADS", Decimal(balance)),
        ]
