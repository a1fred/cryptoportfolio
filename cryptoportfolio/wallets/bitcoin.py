from decimal import Decimal
from typing import List, Tuple

import requests

from cryptoportfolio.wallets.abc import Wallet


class BitcoinWallet(Wallet):
    decimal_places = 18
    symbol = "BTC"

    def _get_addr_coin_balance(self, addr: str) -> Decimal:
        balance_satoshi = requests.get(
            "https://blockchain.info/ru/balance?active=%s" % addr).json()[addr]['final_balance']
        return Decimal(balance_satoshi) / Decimal("100000000")

    def _get_addr_coin_tokens_balance(self, addr: str) -> List[Tuple[str, Decimal]]:
        return []
