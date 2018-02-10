from typing import Tuple, List
from decimal import Decimal

import requests

from cryptoportfolio.interfaces.base import Address


class PoolBitcoinCom(Address):
    decimal_places = 18
    __api_data = None

    def __init__(self, api_key: str, **kwargs) -> None:
        self.api_key = api_key
        super().__init__(**kwargs)

    def _get_api_data(self):
        if not self.__api_data:
            self.__api_data = requests.get(
                "https://console.pool.bitcoin.com/srv/api/user?apikey=%s" % self.api_key).json()
        return self.__api_data

    def _get_addr_coins_and_tokens_balance(self) -> List[Tuple[str, Decimal]]:
        result = self._get_api_data()
        response = []
        if Decimal(result['bitcoinCashBalance']) != Decimal('0.0'):
            response.append(("BCH", Decimal(result['bitcoinCashBalance'])))
        if Decimal(result['bitcoinBalance']) != Decimal('0.0'):
            response.append(("BTC", Decimal(result['bitcoinCashBalance'])))
        return response
