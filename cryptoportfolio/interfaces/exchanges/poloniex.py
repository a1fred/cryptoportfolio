from typing import Tuple, Iterable
from decimal import Decimal
from urllib.parse import urlencode
import time
import hmac
import hashlib

import requests

from cryptoportfolio.interfaces.base import Address


class PoloniexWallet(Address):
    decimal_places = 18
    __api_response = None

    def __init__(self, api_key: str, api_secret: str, **kwargs) -> None:
        self.api_key = api_key
        self.api_secret: str = api_secret
        super().__init__(**kwargs)

    def balance_request(self):
        if self.__api_response is None:
            req = {
                'command': 'returnBalances',
                'nonce': int(time.time() * 1000),
            }
            post_data = urlencode(req)
            sign = hmac.new(self.api_secret.encode(), post_data.encode(), hashlib.sha512).hexdigest()

            self.__api_response = requests.post(
                'https://poloniex.com/tradingApi',
                headers={
                    'Sign': sign,
                    'Key': self.api_key,
                },
                data=req,
            ).json()

        for symbol, balance in self.__api_response.items():
            balance_dec = Decimal(balance)
            if balance_dec != Decimal("0.0"):
                yield symbol, balance_dec

    def _get_addr_coins_and_tokens_balance(self) -> Iterable[Tuple[str, Decimal]]:
        yield from self.balance_request()
