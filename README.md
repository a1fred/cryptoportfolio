# Cryptoportfolio
Show your coins portfilio tool for conky or geektool.  
Can show percentile wallet values if you own only percent of all balance.

## Features
### Supported wallets
* BTC
* ETH, automatically find all tokens
* EMC
* MAGI
* STELLAR, automatically find all tokens

### Supported pools
* nicehash.com
* pool.bitcoin.com

## Setup
### Installation
Clone this repo and run 
```shell
$ python3 setup.py install
```
Maybe upload to pypi later.

### Configure
See settings-sample.py

### Run
Show detailed portfolio
```shell
$ cryptoportfolio ./conf.py
```

Show summary
```shell
$ cryptoportfolio --summary ./conf.py
```

### Sample output
```sh
$ pipenv run python3 main.py -s ./conf.py
BTC 4352.8092 30202532.40$
ETH 2399.3909 1674997.95$
CANDY 153625956.0001 129504.23$
CNX 1000.0000 5728.26$
ACC 352.0962 2671.31$
OMG 218.8423 2099.82$
...
PYN 385.1521 0.00$
MNTP 0.1001 0.00$
AiO 11970.0000 0.00$
ZIBER 468.5654 0.00$
٨ 5300000.0000 0.00$
Total: 32021331.96$
```

# TODO
* Add some tests
* inifile configuration
* Add more coins and pools
* Add siacoin when there is block explorer
