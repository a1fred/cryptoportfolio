from decimal import Decimal

import requests

from cryptoportfolio.interfaces.base import CryptoCoinWallet


class QtumWallet(CryptoCoinWallet):
    decimal_places = 8

    def _get_addr_coins_and_tokens_balance(self):
        balance_qtoshi = requests.get(
            "https://qtum.info/api/address/%s" % self.addr
        ).json()['balance']
        return [
            ("QTUM", Decimal(balance_qtoshi) / Decimal("100000000")),
        ]
