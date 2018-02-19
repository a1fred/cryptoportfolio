import requests
from decimal import Decimal

from cryptoportfolio.interfaces.base import CryptoCoinWallet


class StellarWallet(CryptoCoinWallet):
    decimal_places = 18

    def _get_addr_coins_and_tokens_balance(self):
        data = requests.get(
            "https://horizon.stellar.org/accounts/%s" % self.addr
        ).json()

        res = []
        for b in data['balances']:
            if b['asset_type'] == 'native':
                res.append(('XLM', Decimal(b['balance'])))
            else:
                res.append((b['asset_type'], Decimal(b['balance'])))
        return res
