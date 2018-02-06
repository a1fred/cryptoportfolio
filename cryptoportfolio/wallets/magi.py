from decimal import Decimal
from typing import List, Tuple

import requests

from cryptoportfolio.wallets.abc import Wallet


class MagiWallet(Wallet):
    decimal_places = 18
    symbol = "XMG"

    def _get_addr_coin_balance(self, addr: str) -> Decimal:
        balance = requests.get(
            "https://chainz.cryptoid.info/xmg/api.dws?q=getbalance&a=%s" % addr
        ).text
        return Decimal(balance)

    def _get_addr_coin_tokens_balance(self, addr: str) -> List[Tuple[str, Decimal]]:
        return []
