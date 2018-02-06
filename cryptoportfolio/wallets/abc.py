from typing import List, Tuple, Dict

from decimal import Decimal, ROUND_UP

from cryptoportfolio.lib.coinmarketcap import get_price_usd
from cryptoportfolio.utils.io import format_curr_balance


class Wallet:
    decimal_places: int
    symbol: str

    def __init__(self, name: str, addrs: List[str], percent_owned=Decimal('100'), decimal_places: int=None):
        self.name = name
        self.addrs = addrs
        self.percent_owned = percent_owned / Decimal('100')
        if decimal_places is not None:
            self.decimal_places = decimal_places

    def get_name(self) -> str:
        if self.percent_owned != Decimal('1'):
            return "%s (%.2f%% owned)" % (self.name, self.percent_owned * 100)
        else:
            return self.name

    def format_balance(self, b: Decimal) -> Decimal:
        return format_curr_balance(b, self.decimal_places)

    def get_coin_price_usd(self) -> Decimal:
        return get_price_usd(self.symbol)

    def get_token_price_usd(self, token_symbol) -> Decimal:
        return get_price_usd(token_symbol)

    def get_coin_balance(self) -> List[Tuple[str, Decimal]]:
        """
        :return: [
            ("0xETHADDR", Decimal("23.0")),
            ...
        ]
        """
        result = []
        for addr in self.addrs:
            balance = self._get_addr_coin_balance(addr)
            result.append((addr, balance * self.percent_owned))
        return result

    def get_coin_tokens_balance(self, include_coin_balance=False) -> Dict[str, List[Tuple[str, Decimal]]]:
        """
        :return: {
            "0xETHADDR": [
                ("EOS": Decimal("10.0")),
                ...
            ],
            ...
        }
        """

        result = {}
        for addr in self.addrs:
            tokens_balances = self._get_addr_coin_tokens_balance(addr)
            result[addr] = [(s, b * self.percent_owned) for s, b in tokens_balances]
            if include_coin_balance:
                result[addr].insert(0, (self.symbol, self._get_addr_coin_balance(addr) * self.percent_owned))
        return result

    def _get_addr_coin_balance(self, addr: str) -> Decimal:
        raise NotImplementedError

    def _get_addr_coin_tokens_balance(self, addr: str) -> List[Tuple[str, Decimal]]:
        raise NotImplementedError
