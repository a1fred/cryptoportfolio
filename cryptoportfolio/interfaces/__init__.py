from cryptoportfolio.interfaces.miningpools import (
    nicehash,
    pool_bitcoin_com,
    f2pool
)

from cryptoportfolio.interfaces.wallets import (
    bitcoin,
    emercoin,
    ethereum,
    magi,
    stellar,
    nem,
    radium,
    reddcoin,
    hyperstake,
    cardano,
    crds,
)

from cryptoportfolio.interfaces.exchanges import (
    poloniex,
    bittrex,
    binance,
)


INTERFACES_MAPPING = {
    'f2pool': f2pool.F2PoolWallet,
    'nicehash': nicehash.NicehashWallet,
    'bitcoin_com': pool_bitcoin_com.PoolBitcoinCom,
    'bitcoin': bitcoin.BitcoinWallet,
    'emercoin': emercoin.EmercoinWallet,
    'ethereum': ethereum.EthereumWallet,
    'magi': magi.MagiWallet,
    'stellar': stellar.StellarWallet,
    'poloniex': poloniex.PoloniexWallet,
    'bittrex': bittrex.BittrexWallet,
    'binance': binance.BinanceWallet,
    'nem': nem.NemWallet,
    'radium': radium.RadiumWallet,
    'reddcoin': reddcoin.ReddcoinWallet,
    'hyperstake': hyperstake.HyperstakeWallet,
    'cardano': cardano.CardanoWallet,
    'crds': crds.CreditsWallet,
}
