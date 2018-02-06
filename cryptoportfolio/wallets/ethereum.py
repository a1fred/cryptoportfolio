from decimal import Decimal
from typing import List, Tuple

import requests

from cryptoportfolio.wallets.abc import Wallet


class EthereumWallet(Wallet):
    decimal_places = 18
    symbol = "ETH"
    __ethplorer_data = None

    def _get_ethplorer_data(self, addr):
        if not self.__ethplorer_data:
            self.__ethplorer_data = requests.get(
                "https://api.ethplorer.io/getAddressInfo/%s?apiKey=freekey" % addr
            ).json()
        return self.__ethplorer_data

    def _get_addr_coin_balance(self, addr: str) -> Decimal:
        return Decimal(self._get_ethplorer_data(addr)['ETH']['balance'])

    def _get_addr_coin_tokens_balance(self, addr: str) -> List[Tuple[str, Decimal]]:
        results = []
        data = self._get_ethplorer_data(addr)
        for token in data['tokens']:
            symbol = token['tokenInfo']['symbol']
            amount = token['balance'] * pow(10, -int(token['tokenInfo']['decimals']))
            results.append((symbol, Decimal(amount)))
        return results
