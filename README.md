# Cryptoportfolio
Tool for show your coins portfilio. Easily integrates with
[conky](https://github.com/brndnmtthws/conky) or 
[geektool](https://www.tynsoe.org/v2/geektool/).  


### Features
* support popular coins
* support mining pool balance
* automatically find all tokens on eth or stellar wallets
* create percentile wallet if you own only percent of all balance
* simple api easy to use as library in your project

Supported wallets:
* BTC
* ETH, automatically find all tokens
* EMC
* MAGI
* STELLAR, automatically find all tokens

Supported pools:
* nicehash.com
* pool.bitcoin.com

### Set up
##### Installation
###### From source
###### From [pypi](https://pypi.python.org/pypi/cryptoportfolio)
```shell
$ pip3 install cryptoportfolio
```
Clone this repo and run 
```shell
$ python3 setup.py install
```

##### Configure
See example in [sample.yml](sample.yml)

##### Run
Flags
```sh
$ cryptoportfolio -h
positional arguments:
  settings_path

optional arguments:
  -h, --help            show this help message and exit
  -s, --summarize       Summarize same currencies in one row
  -z, --hide-zeros      Hide zero crypto balances
  --sort                Sort by USD balance
  --hide-usd-zeros      Hide zero USD balances
  -T, --print-all-total
                        Print all total USD
  -t, --print-group-total
                        Print group total USD

```
Show detailed portfolio
```shell
$ cryptoportfolio ./conf.yml
```

Show summary
```shell
$ cryptoportfolio --summary ./conf.yml
```
Sample output:
```sh
$ python3 main.py -s ./conf.yml
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
* Better configuration documentation
* Maybe python2 support because its mac os default
* Add more coins and pools
* Add siacoin when there is block explorer
* Add simple coin/token tickers without wallet
