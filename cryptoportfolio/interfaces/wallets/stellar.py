from typing import List, Tuple

import requests
from decimal import Decimal

from cryptoportfolio.interfaces.base import CryptoCoinWallet


class StellarWallet(CryptoCoinWallet):
    decimal_places = 18
    symbol = "XLM"

    def _get_addr_coin_balance(self) -> Decimal:
        data = requests.get(
            "https://horizon.stellar.org/accounts/%s" % self.addr
        ).json()

        balance = Decimal('0.0')
        for b in data['balances']:
            if b['asset_type'] == 'native':
                balance += Decimal(b['balance'])
        return balance

    def _get_addr_coin_tokens_balance(self) -> List[Tuple[str, Decimal]]:
        data = requests.get(
            "https://horizon.stellar.org/accounts/%s" % self.addr
        ).json()

        res = []
        for b in data['balances']:
            if b['asset_type'] != 'native':
                res.append((b['asset_type'], Decimal(b['balance'])))
        return res
