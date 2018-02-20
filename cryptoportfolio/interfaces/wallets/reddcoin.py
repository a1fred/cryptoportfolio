from decimal import Decimal

import requests

from cryptoportfolio.interfaces.base import CryptoCoinWallet


class ReddcoinWallet(CryptoCoinWallet):
    decimal_places = 18

    def _get_addr_coins_and_tokens_balance(self):
        balance = requests.get(
            "https://live.reddcoin.com/api/addr/%s" % self.addr
        ).json()['balance']
        return [
            ("RDD", Decimal(balance)),
        ]
