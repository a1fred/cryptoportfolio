from decimal import Decimal
from cryptoportfolio.lib.bittrex import Bittrex, API_V2_0

from cryptoportfolio.interfaces.base import Address


class BittrexWallet(Address):
    decimal_places = 18
    __api_response = None

    def __init__(self, api_key, api_secret, **kwargs):
        self.bittrex = Bittrex(api_key, api_secret, api_version=API_V2_0)
        super(BittrexWallet, self).__init__(**kwargs)

    def balance_request(self):
        resp = self.bittrex.get_balances()

        if 'result' in resp and resp['result']:
            for curr in resp['result']:
                symbol = curr['Currency']['Currency']
                balance = Decimal(curr['Balance']['Balance'])
                if balance != 0.0:
                    yield (symbol, balance)

    def _get_addr_coins_and_tokens_balance(self):
        for balance_item in self.balance_request():
            yield balance_item
