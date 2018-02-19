from decimal import Decimal

import requests

from cryptoportfolio.interfaces.base import CryptoCoinWallet


class EthereumWallet(CryptoCoinWallet):
    decimal_places = 18
    __ethplorer_data = None

    def _get_ethplorer_data(self):
        if not self.__ethplorer_data:
            self.__ethplorer_data = requests.get(
                "https://api.ethplorer.io/getAddressInfo/%s?apiKey=freekey" % self.addr
            ).json()
        return self.__ethplorer_data

    def _get_addr_coins_and_tokens_balance(self):
        results = []
        data = self._get_ethplorer_data()

        results.append(
            ('ETH', Decimal(self._get_ethplorer_data()['ETH']['balance']))
        )

        if 'tokens' in data:
            for token in data['tokens']:
                symbol = token['tokenInfo']['symbol']
                amount = token['balance'] * pow(10, -int(token['tokenInfo']['decimals']))
                results.append((symbol, Decimal(amount)))
        return results
