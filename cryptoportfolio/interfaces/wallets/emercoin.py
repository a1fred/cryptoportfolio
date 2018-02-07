from decimal import Decimal
from typing import List, Tuple

import requests

from cryptoportfolio.interfaces.base import CryptoCoinWallet


class EmercoinWallet(CryptoCoinWallet):
    decimal_places = 18
    symbol = "EMC"

    def _get_addr_coin_balance(self) -> Decimal:
        data = requests.get(
            "https://emercoin.mintr.org/api/address/balance/%s" % self.addr
        ).json()
        return Decimal(data['balance'])

    def _get_addr_coin_tokens_balance(self) -> List[Tuple[str, Decimal]]:
        return []
