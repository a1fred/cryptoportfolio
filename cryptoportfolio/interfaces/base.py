from typing import List, Tuple

from decimal import Decimal

from cryptoportfolio.lib.coinmarketcap import get_price_usd
from cryptoportfolio.utils.io import format_curr_balance


class Address:
    decimal_places: int
    symbol: str

    def __init__(self, percent_owned=Decimal('100'), decimal_places: int=None, name=None) -> None:
        self.percent_owned = Decimal(percent_owned) / Decimal('100')
        if decimal_places is not None:
            self.decimal_places = int(decimal_places)
        self.name = name

    def format_balance(self, b: Decimal) -> Decimal:
        return format_curr_balance(b, self.decimal_places)

    def get_coins_and_tokens_balance(self) -> List[Tuple[str, Decimal]]:
        """
        :return: [
            ("EOS": Decimal("10.0")),
            ...
        ]
        """

        result = []
        tokens_balances = self._get_addr_coins_and_tokens_balance()
        for token_symbol, balance in tokens_balances:
            result.append((token_symbol, balance * self.percent_owned))
        return result

    def _get_addr_coins_and_tokens_balance(self,) -> List[Tuple[str, Decimal]]:
        raise NotImplementedError


class CryptoCoinWallet(Address):
    def __init__(self, addr: str, **kwargs) -> None:
        self.addr = addr
        super().__init__(**kwargs)
