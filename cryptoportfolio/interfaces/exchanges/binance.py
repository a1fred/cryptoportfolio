from decimal import Decimal
import time
import hashlib
import hmac
from operator import itemgetter

import requests

from cryptoportfolio.interfaces.base import Address


class BinanceWallet(Address):
    decimal_places = 18
    __api_response = None

    def __init__(self, api_key, api_secret, **kwargs):
        self.api_key = api_key
        self.api_secret = api_secret

        self.session = requests.Session()
        self.session.headers.update({'Accept': 'application/json', 'X-MBX-APIKEY': self.api_key})
        super(BinanceWallet, self).__init__(**kwargs)

    def _generate_signature(self, ordered_data):
        query_string = '&'.join(["{}={}".format(d[0], d[1]) for d in ordered_data.items()])
        m = hmac.new(self.api_secret.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256)
        return m.hexdigest()

    def _request(self, method, uri):
        params = {'timestamp': int(time.time() * 1000)}
        params['signature'] = self._generate_signature(params)

        response = getattr(self.session, method)(uri, params=params, timeout=10)
        return response.json()

    def _get_addr_coins_and_tokens_balance(self):
        resp = self._request('get', "https://api.binance.com/api/v3/account")
        if 'balances' in resp and resp['balances']:
            for asset in resp['balances']:
                balance = Decimal(asset['free'])
                if balance != 0:
                    yield asset['asset'], balance
