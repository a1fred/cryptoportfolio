from decimal import Decimal

import requests

from cryptoportfolio.interfaces.base import CryptoCoinWallet


class CreditsWallet(CryptoCoinWallet):
    decimal_places = 18

    def _get_addr_coins_and_tokens_balance(self):
        balance = requests.get("http://explorer.crds.co/ext/getbalance/%s" % self.addr).text
        return [
            ("CRDS", Decimal(balance)),
        ]
