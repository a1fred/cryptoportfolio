from decimal import Decimal

import requests

from cryptoportfolio.interfaces.base import CryptoCoinWallet


class EmercoinWallet(CryptoCoinWallet):
    decimal_places = 18

    def _get_addr_coins_and_tokens_balance(self):
        data = requests.get(
            "https://explorer.emercoin.com/api/address/balance/%s" % self.addr
        ).json()
        return [
            ("EMC", Decimal(data['balance'])),
        ]
