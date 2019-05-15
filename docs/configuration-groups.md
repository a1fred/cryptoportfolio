# Groups configuration

Fast example:
```yml
groups:
  test:
    - interface: ethereum
      addr: 0xe99356bde974bbe08721d77712168fa070aa8da4
      decimal_places: 4
      name: home mist
      percent_owned: 100
```

## Universal options
Universal options can be set in `defaults` file section.
Every option from defaults section appying to each group element
if it has not set permanently.
Values can be applied to any wallet:
 * `interface` required, string
    coin interface name. Coins list below.
 * `decimal_places` optional, int
    Decimal places for cryptocurrency balance output
 * `percent_owned`: optional, int
    Balance percentile you own
 * `name` optional, string
    Short name for wallet

## Wallets
cryptoportfolio can show your cryptocoin wallet balances.

#### [Bitcoin](https://bitcoin.org/)
Bitcoin address
Interface name: `bitcoin`
Works using [https://blockchain.info](https://blockchain.info)
Options:
 * [universal options](#universal-options)
 * `addr` required, string
    Bitcoin address

#### [Ethereum](https://ethereum.org/)
Ethereum address
Interface name: `ethereum`
Works using [https://api.ethplorer.io](https://api.ethplorer.io)
Options:
 * [universal options](#universal-options)
 * `addr` required, string
    Ethereum address

#### [Emercoin](https://emercoin.com/)
Emercoin address
Interface name: `emercoin`
Works using [https://emercoin.mintr.org](https://emercoin.mintr.org)
Options:
 * [universal options](#universal-options)
 * `addr` required, string
    Emercoin address

#### [MAGI](http://www.m-core.org/)
MAGI coin address
Interface name: `magi`
Works using [https://chainz.cryptoid.info](https://chainz.cryptoid.info)
Options:
 * [universal options](#universal-options)
 * `addr` required, string
    magi coin address

#### [Stellar lumens](https://www.stellar.org/)
Stellar address
Interface name: `stellar`
Works using [https://horizon.stellar.org](https://horizon.stellar.org)
Options:
 * [universal options](#universal-options)
 * `addr` required, string
    stellar address

#### [NEM](https://nem.io/)
NEM address
Interface name: `nem`
Works using undocumnted balance request on [http://explorer.ournem.com/](http://explorer.ournem.com/)
Options:
 * [universal options](#universal-options)
 * `addr` required, string
    nem wallet address


#### [Reddcoin](https://www.reddcoin.com/)
Reddcoin address
Interface name: `reddcoin`
Works using undocumnted balance request on [https://live.reddcoin.com/](https://live.reddcoin.com/)
Options:
 * [universal options](#universal-options)
 * `addr` required, string
    reddcoin wallet address


#### [Radium](https://radiumcore.org/)
Radium address
Interface name: `reddcoin`
Works using api balance request on [https://chainz.cryptoid.info/](https://chainz.cryptoid.info/)
Options:
 * [universal options](#universal-options)
 * `addr` required, string
    radium wallet address


#### [Hyperstake](http://hyperstake.io/)
Hyperstake address
Interface name: `hyperstake`
Works using balance request on [https://prohashing.com/explorer/](https://prohashing.com/explorer/)
Options:
 * [universal options](#universal-options)
 * `addr` required, string
    hyperstake wallet address

#### [Cardano](https://www.cardanohub.org/)
Cardano address
Interface name: `cardano`
Works using balance request on [https://cardanoexplorer.com](https://cardanoexplorer.com)
Options:
 * [universal options](#universal-options)
 * `addr` required, string
    cardano wallet address

#### [QTUM](https://qtum.org)
QTUM address
Interface name: `qtum`
Works using official explorer api [https://qtum.info/](https://github.com/qtumproject/qtuminfo/blob/master/packages/qtuminfo-api/README.md)
Options:
 * [universal options](#universal-options)
 * `addr` required, string
    qtum wallet address


#### [Credits (CRDS)](https://crds.co/)
CRDS address
Interface name: `crds`
Works using official explorer api [http://explorer.crds.co/](http://explorer.crds.co/)
Options:
 * [universal options](#universal-options)
 * `addr` required, string
    CRDS wallet address


# Mining pools
cryptoportfolio can show your mining pool confirmed balance.

#### [Nicehash](https://www.nicehash.com/)
Interface name: `nicehash`
Works using [nicehash api](https://www.nicehash.com/doc-api)
You can get api key and id in [account settings page](https://www.nicehash.com/settings/api)
Options:
 * [universal options](#universal-options)
 * `id` required, string
    api id
 * `key` required, string
     api key

#### [pool.bitcoin.com](https://pool.bitcoin.com/index_en.html)
Interface name: `bitcoin_com`
Works using [rest v2 api](https://console.pool.bitcoin.com/apidoc/index.html)
You can get api_key [account settings page](https://console.pool.bitcoin.com/settings)
Options:
 * [universal options](#universal-options)
 * `api_key` required, string
    api key

#### [f2pool.com](https://www.f2pool.com/)
Interface name: `f2pool`
Works using [rest api](https://www.f2pool.com/developer/api)
Options:
 * [universal options](#universal-options)
 * `currency` required, string
   Your currency
 * `user` required, string
   Username

## Exchanges
cryptoportfolio can show your exchange deposits

#### [poloniex.com](https://poloniex.com/)
Interface name: `poloniex`
Works using [api](https://poloniex.com/support/api/)
You can get api keys in [api settings page](https://poloniex.com/apiKeys)
Options:
 * [universal options](#universal-options)
 * `api_key` required, string
   API key
 * `api_secret` required, string
   API secret

#### [bittrex.com](https://bittrex.com)
Interface name: `bittrex`
Works using [python-bittrex api wrapper](https://github.com/ericsomdahl/python-bittrex)
You can get api keys in [api settings page](https://bittrex.com/Manage#sectionApi)
Options:
 * [universal options](#universal-options)
 * `api_key` required, string
   API key
 * `api_secret` required, string
   API secret

#### [binance.com](https://binance.com)
Interface name: `binance`
Works using [official api](https://github.com/binance-exchange/binance-official-api-docs/blob/master/rest-api.md)
You can get api keys in [api settings page](https://www.binance.com/userCenter/createApi.html)
Options:
 * [universal options](#universal-options)
 * `api_key` required, string
   API key
 * `api_secret` required, string
   API secret

## Example
```yml
groups:
  test:
    - interface: ethereum
      addr: 0xe99356bde974bbe08721d77712168fa070aa8da4
      percent_owned: 80
    - interface: bitcoin
      addr: 1Hz96kJKF2HLPGY15JWLB5m9qGNxvt8tHJ
      percent_owned: 10
    - interface: magi
      decimal_places: 4
      addr: 958cdNtPsrU5ohF2qULhnSFkdu99JCrDgv
    - interface: stellar
      addr: GAKOQTDQYEV4KZI2EGEL4OS4AA6XHAXFQUAJ52C7B4H7SCL2XVKQYJAR
    - interface: emercoin
      addr: EQcFiCWANf3jziUumewwuTHMzMxa4a4QDw

    - interface: nicehash
      name: nicehash
      id: ...
      key: ...
    - interface: bitcoin_com
      api_key: ...

    - interface: poloniex
      name: poloniex
      api_key: ...
      api_secret: ...
```
