from typing import List, Tuple

import requests
from decimal import Decimal

from cryptoportfolio.wallets.abc import Wallet


class StellarWallet(Wallet):
    decimal_places = 18
    symbol = "XLM"

    def _get_addr_coin_balance(self, addr: str) -> Decimal:
        data = requests.get(
            "https://horizon.stellar.org/accounts/%s" % addr
        ).json()

        balance = Decimal('0.0')
        for b in data['balances']:
            if b['asset_type'] == 'native':
                balance += Decimal(b['balance'])
        return balance

    def _get_addr_coin_tokens_balance(self, addr: str) -> List[Tuple[str, Decimal]]:
        data = requests.get(
            "https://horizon.stellar.org/accounts/%s" % addr
        ).json()

        res = []
        for b in data['balances']:
            if b['asset_type'] != 'native':
                res.append((b['asset_type'], Decimal(b['balance'])))
        return res
