import requests
from decimal import Decimal

from cryptoportfolio.interfaces.base import CryptoCoinWallet


class HyperstakeWallet(CryptoCoinWallet):
    """
    Uses undocumented request
    """
    decimal_places = 18

    def _get_addr_coins_and_tokens_balance(self):
        data = requests.get(
            "https://prohashing.com/explorerJson/getAddress?address=%s&coin_id=184" % self.addr
        ).json()

        return [
            ("HYP", Decimal(data['balance'])),
        ]
