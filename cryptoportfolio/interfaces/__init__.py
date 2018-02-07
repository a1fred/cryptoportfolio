from cryptoportfolio.interfaces.miningpools import (
    nicehash,
    pool_bitcoin_com,
)

from cryptoportfolio.interfaces.wallets import (
    bitcoin,
    emercoin,
    ethereum,
    magi,
    stellar,
)


INTERFACES_MAPPING = {
    'nicehash': nicehash.NicehashWallet,
    'bitcoin_com': pool_bitcoin_com.PoolBitcoinCom,
    'bitcoin': bitcoin.BitcoinWallet,
    'emercoin': emercoin.EmercoinWallet,
    'ethereum': ethereum.EthereumWallet,
    'magi': magi.MagiWallet,
    'stellar': stellar.StellarWallet,
}
