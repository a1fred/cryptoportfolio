import unittest

from decimal import Decimal

from cryptoportfolio.lib.convert import coinmarketcap


class CoinmarketcapTests(unittest.TestCase):
    def assertCoinExists(self, symbol):
        price_usd = coinmarketcap.get_price_usd(symbol)
        self.assertIsInstance(price_usd, Decimal)
        self.assertGreater(price_usd, 0)

    def test_tickers(self):
        self.assertCoinExists("BTC")
        self.assertCoinExists("ETH")
