import requests
from decimal import Decimal

from cryptoportfolio.interfaces.base import CryptoCoinWallet


class NemWallet(CryptoCoinWallet):
    """
    Uses undocumented request
    """
    decimal_places = 18

    def _get_addr_coins_and_tokens_balance(self):
        data = requests.post(
            "http://explorer.ournem.com/account/detail",
            headers={
                "Content-Type": "application/json",
            },
            data='{"address": "%s"}' % str(self.addr).replace('-', '')
        ).json()
        if data == 'Not Found':
            return [
                ("XEM", Decimal("0.0")),
            ]

        return [
            ("XEM", Decimal(data['balance']) * Decimal("0.000001")),
        ]
