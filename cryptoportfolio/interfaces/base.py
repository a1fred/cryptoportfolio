from decimal import Decimal

from cryptoportfolio.utils.io import format_curr_balance


class Address(object):
    decimal_places = None  # type: int
    symbol = None

    def __init__(self, percent_owned=Decimal('100'), decimal_places=None, name=None):
        self.percent_owned = Decimal(percent_owned) / Decimal('100')
        if decimal_places is not None:
            self.decimal_places = int(decimal_places)
        self.name = name

    def format_balance(self, b):
        return format_curr_balance(b, self.decimal_places)

    def get_coins_and_tokens_balance(self):
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

    def _get_addr_coins_and_tokens_balance(self):
        raise NotImplementedError


class CryptoCoinWallet(Address):
    def __init__(self, addr, **kwargs):
        self.addr = addr
        super(CryptoCoinWallet, self).__init__(**kwargs)
