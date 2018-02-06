from decimal import Decimal
from typing import List, Tuple

import requests

from cryptoportfolio.wallets.abc import Wallet


class EmercoinWallet(Wallet):
    decimal_places = 18
    symbol = "EMC"

    def _get_addr_coin_balance(self, addr: str) -> Decimal:
        data = requests.get(
            "https://emercoin.mintr.org/api/address/balance/%s" % addr
        ).json()
        return Decimal(data['balance'])

    def _get_addr_coin_tokens_balance(self, addr: str) -> List[Tuple[str, Decimal]]:
        return []
