# Configuration manual
Each configuration file need to have not empty tickers or groups section.

Config file writes in YML and has three sections:
 * defaults
 * groups
 * tickers

## Defaults
Key-value map with default values, that applying
on *every* group in configuration.
Possible values:
 * `decimal_places` int  
   Decimal places for cryptocurrency balance output
 * `percent_owned`: int  
    Balance percentile you own

For example, if we have nicehash account with our friend, 50/50 owned
and withdraw earnings to BTC wallet:
```yml
defaults:
   percent_owned: 50
   decimal_places: 4
groups:
  groupfarm:
    - interface: nicehash
      name: nicehash
      id: 8
      key: secret
    - interface: bitcoin
      addr: <btc_addr>
```

if we have 1 btc at nicehash and 2 btc at wallet, 
cryptoportfolio shows us:

```sh
             groupfarm
BTC            0.5000    $4000.00
BTC (nicehash) 1.0000    $8000.00
Total: $12000.00
```


## Groups
Wallet grouts, we want to see balance and usd value.  
Array of hashmaps, where every mapping represents one wallet, that we want to see.  
See more info about using wallets here [configuration-groups.md](configuration-groups.md) 

Fast example:
```yml
groups:
  groupfarm:
    - interface: nicehash
      name: nicehash
      id: 8
      key: secret
    - interface: bitcoin
      addr: <btc_addr>
```

## Tickers
Use this if dont have wallet, or have not coins, but want to see usd price.  
Array of strings, where string is coin symbol.

Example:
```yml
tickers:
  - BTC
  - ETH
```

This will show BTC and ETH usd price.

## Full configuration example:
```yml
defaults:
  decimal_places: 4

groups:
  test:
    - interface: ethereum
      addr: 0xe99356bde974bbe08721d77712168fa070aa8da4
    - interface: bitcoin
      addr: 1Hz96kJKF2HLPGY15JWLB5m9qGNxvt8tHJ
      percent_owned: 10
    - interface: magi
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
      name: bitcoin.com
      api_key: ...

tickers:
  - RADS
  - EOS
```

Output:
```sh
cryptoportfolio ~/cryptoportfolio.yml -s --sort
               test
BTC (nicehash)      2.0064   8051.27
EMC               216.4263   58.39
ETH                 0.0416   33.33
BTC (bitcoin.com)   0.0016   13.43
XMG                 0.5640   0.22
VIU (mist)          2.8487   0.07
INSP (mist)       777.0000   0.00

Tickers:
 * RADS $5.51523
 * EOS  $7.87042
```
