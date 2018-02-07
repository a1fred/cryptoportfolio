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
        self.name = name or self.symbol

    def format_balance(self, b: Decimal) -> Decimal:
        return format_curr_balance(b, self.decimal_places)

    def get_coin_price_usd(self) -> Decimal:
        return get_price_usd(self.symbol)

    def get_token_price_usd(self, token_symbol) -> Decimal:
        return get_price_usd(token_symbol)

    def get_coin_balance(self) -> Tuple[str, Decimal]:
        """
        :return: ("0xETHADDR", Decimal("23.0")),
        """
        balance = self._get_addr_coin_balance()
        return self.symbol, balance * self.percent_owned

    def get_coin_tokens_balance(self, include_coin_balance=False) -> List[Tuple[str, Decimal]]:
        """
        :return: [
            ("EOS": Decimal("10.0")),
            ...
        ]
        """

        result = []
        tokens_balances = self._get_addr_coin_tokens_balance()
        for token_symbol, balance in tokens_balances:
            result.append((token_symbol, balance * self.percent_owned))
        if include_coin_balance:
            result.insert(0, (self.symbol, self._get_addr_coin_balance() * self.percent_owned))
        return result

    def _get_addr_coin_balance(self) -> Decimal:
        raise NotImplementedError

    def _get_addr_coin_tokens_balance(self,) -> List[Tuple[str, Decimal]]:
        raise NotImplementedError


class CryptoCoinWallet(Address):
    def __init__(self, addr: str, **kwargs) -> None:
        self.addr = addr
        super().__init__(**kwargs)
