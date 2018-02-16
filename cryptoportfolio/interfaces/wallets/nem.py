from typing import List, Tuple

import requests
from decimal import Decimal

from cryptoportfolio.interfaces.base import CryptoCoinWallet


class NemWallet(CryptoCoinWallet):
    """
    Uses undocumented request
    """
    decimal_places = 18

    def _get_addr_coins_and_tokens_balance(self) -> List[Tuple[str, Decimal]]:
        data = requests.post(
            "http://explorer.ournem.com/account/detail",
            headers={
                "Content-Type": "application/json",
            },
            data='{"address": "%s"}' % str(self.addr).replace('-', '')
        ).json()

        return [
            ("XEM", Decimal(data['balance']) * Decimal("0.000001")),
        ]
