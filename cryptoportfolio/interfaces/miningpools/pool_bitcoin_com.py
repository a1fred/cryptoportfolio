from typing import Tuple, List
from decimal import Decimal

import requests

from cryptoportfolio.interfaces.base import Address


class PoolBitcoinCom(Address):
    decimal_places = 18
    symbol = "BTC"

    def __init__(self, api_key: str, **kwargs) -> None:
        self.api_key = api_key
        super().__init__(**kwargs)

    __api_data = None

    def _get_api_data(self):
        if not self.__api_data:
            self.__api_data = requests.get(
                "https://console.pool.bitcoin.com/srv/api/user?apikey=%s" % self.api_key).json()
        return self.__api_data

    def _get_addr_coin_tokens_balance(self) -> List[Tuple[str, Decimal]]:
        result = self._get_api_data()
        if Decimal(result['bitcoinCashBalance']) != Decimal('0.0'):
            return [
                ("BCH", Decimal(result['bitcoinCashBalance'])),
            ]
        else:
            return []

    def _get_addr_coin_balance(self) -> Decimal:
        result = self._get_api_data()
        return Decimal(result['bitcoinBalance'])
