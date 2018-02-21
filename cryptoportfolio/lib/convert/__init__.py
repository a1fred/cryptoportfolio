from cryptoportfolio.lib.convert import (
    coinmarketcap,
    cryptocompare,
)


CONVERTORS_MAPPING = {
    'coinmarketcap': coinmarketcap.get_price_usd,
    'cryptocompare': cryptocompare.get_price_usd,
}
