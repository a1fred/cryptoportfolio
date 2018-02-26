from decimal import Decimal

import requests

from cryptoportfolio.interfaces.base import CryptoCoinWallet


class CardanoWallet(CryptoCoinWallet):
    decimal_places = 18

    def _get_addr_coins_and_tokens_balance(self):
        balance_data = requests.get("https://cardanoexplorer.com/api/addresses/summary/%s" % self.addr).json()
        balance = balance_data['Right']['caBalance']['getCoin']
        return [
            ("ADA", Decimal(balance) / Decimal(1000000)),
        ]
