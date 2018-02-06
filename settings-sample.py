from decimal import Decimal

from cryptoportfolio.wallets import (
    bitcoin,
    ethereum,
)

from cryptoportfolio.miningpools import (
    nicehash,
    pool_bitcoin_com,
)

WALLETS = [
    ethereum.EthereumWallet('ETH', ['0xb6aac3b56ff818496b747ea57fcbe42a9aae6218', ]),
    bitcoin.BitcoinWallet('BTC', ['1N52wHoVR79PMDishab2XmRHsbekCdGquK', ], ),
    nicehash.NicehashWallet("Nicehash", ('key id', 'secret')),
    pool_bitcoin_com.PoolBitcoinCom(
        'Bitcoin.com', 'api-key',
        percent_owned=Decimal('50'),
        decimal_places=4,
    )
]
