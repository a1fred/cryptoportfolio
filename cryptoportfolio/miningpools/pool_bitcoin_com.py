from typing import Tuple, List
from decimal import Decimal

import requests

from cryptoportfolio.wallets.abc import Wallet

NICEHASH_ADDRS = [
    # Id, key

]


class PoolBitcoinCom(Wallet):
    decimal_places = 18
    symbol = "BTC"

    def __init__(self, name: str, api_key: str, percent_owned=Decimal('100'), decimal_places: int=None):
        self.api_key = api_key
        super().__init__(name=name, addrs=[name, ], percent_owned=percent_owned, decimal_places=decimal_places)

    __api_data = None

    def _get_api_data(self):
        if not self.__api_data:
            self.__api_data = requests.get(
                "https://console.pool.bitcoin.com/srv/api/user?apikey=%s" % self.api_key).json()
        return self.__api_data

    def _get_addr_coin_tokens_balance(self, addr: str) -> List[Tuple[str, Decimal]]:
        result = self._get_api_data()
        if Decimal(result['bitcoinCashBalance']) != Decimal('0.0'):
            return [
                ("BCH", Decimal(result['bitcoinCashBalance'])),
            ]
        else:
            return []

    def _get_addr_coin_balance(self, addr: str) -> Decimal:
        result = self._get_api_data()
        return Decimal(result['bitcoinBalance'])
