# Cryptoportfolio
[![Build Status](https://travis-ci.org/a1fred/cryptoportfolio.svg?branch=master)](https://travis-ci.org/a1fred/cryptoportfolio)
[![PyPI version](https://badge.fury.io/py/cryptoportfolio.svg)](https://badge.fury.io/py/cryptoportfolio)
[![PyPI](https://img.shields.io/pypi/pyversions/cryptoportfolio.svg)](https://pypi.python.org/pypi/cryptoportfolio/0.2.7)


Tool for show your coins portfilio. Easily integrates with
[conky](https://github.com/brndnmtthws/conky) or 
[geektool](https://www.tynsoe.org/v2/geektool/).  


### Features
* Show balance on coin wallets,exchanges and mining pools
* Automatically find all tokens on ethereum or stellar wallets
* Show your owned balance from shared wallet by settings percent-owned
* Simple api easy to use as library in your project
* Coins and tokens information from [https://coinmarketcap.com/](https://coinmarketcap.com/)

### Supported wallets:
Cryptoportfolio can show your coins from wallets and mining pools.  
See full list of supported coins in [configuration-groups](docs/configuration-groups.md)  

### Set up
##### Installation
```shell
$ pip3 install cryptoportfolio
```

##### Configure
Read [configuration](docs/configuration.md) and [configuration-groups](docs/configuration-groups.md) for detailed info.  
Fast example in [sample.yml](sample.yml)

##### Run
Read [commandline](docs/commandline.md) for commandline options and flags. Or simply run `cryptoportfolio --help`

Show portfolio
```shell
$ cryptoportfolio ./conf.yml --sort -T
BTC    4352.8092      30202532.40$
ETH    2399.3909      1674997.95$
CANDY  153625956.0001 129504.23$
CNX    1000.0000      5728.26$
ACC    352.0962       2671.31$
OMG    218.8423       2099.82$
...
PYN    385.1521       0.00$
MNTP   0.1001         0.00$
AiO    11970.0000     0.00$
ZIBER  468.5654       0.00$
٨      5300000.0000   0.00$
Total: 32021331.96$
```

### TODO
* Add more coins and pools
* Add siacoin when there is block explorer
* Docs for library usage
