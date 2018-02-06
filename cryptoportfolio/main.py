#!/usr/bin/python
from decimal import Decimal

from cryptoportfolio.lib.coinmarketcap import get_price_usd
from cryptoportfolio.utils.io import format_usd, format_curr_balance
from settings import WALLETS


def print_detail():
    total_usd = Decimal('0.00000')

    for wallet in WALLETS:
        print("%s:" % wallet.get_name())
        curr_dict = {}
        for addr, coin_and_tokens_amount in wallet.get_coin_tokens_balance(include_coin_balance=True).items():
            for symbol, balance in coin_and_tokens_amount:
                balance_usd = get_price_usd(symbol) * balance
                if symbol not in curr_dict:
                    curr_dict[symbol] = {
                        'balance_usd': balance_usd,
                        'balance': balance,
                        'decimal_places': wallet.decimal_places,
                    }
                else:
                    curr_dict[symbol]['balance'] += balance
                    curr_dict[symbol]['balance_usd'] += balance_usd
        for symbol, data in reversed(sorted(curr_dict.items(), key=lambda x: x[1]['balance_usd'])):
            balance = data['balance']
            balance_usd = data['balance_usd']
            decimal_places = data['decimal_places']
            total_usd += balance_usd
            print(" * {symbol} {balance} {balance_usd}$".format(
                symbol=symbol,
                balance=format_curr_balance(balance, decimal_places),
                balance_usd=format_usd(balance_usd),
            ))
    print("Total: %s$" % format_usd(total_usd))


def print_summary():
    total_usd = Decimal('0.0')

    curr_dict = {}
    for wallet in WALLETS:
        for addr, coin_and_tokens_amount in wallet.get_coin_tokens_balance(include_coin_balance=True).items():
            for symbol, balance in coin_and_tokens_amount:
                balance_usd = get_price_usd(symbol) * balance
                if symbol not in curr_dict:
                    curr_dict[symbol] = {
                        'balance_usd': balance_usd,
                        'balance': balance,
                        'decimal_places': wallet.decimal_places,
                    }
                else:
                    curr_dict[symbol]['balance'] += balance
                    curr_dict[symbol]['balance_usd'] += balance_usd
    for symbol, data in reversed(sorted(curr_dict.items(), key=lambda x: x[1]['balance_usd'])):
        balance = data['balance']
        balance_usd = data['balance_usd']
        decimal_places = data['decimal_places']
        total_usd += balance_usd
        print("{symbol} {balance} {balance_usd}$".format(
            symbol=symbol,
            balance=format_curr_balance(balance, decimal_places),
            balance_usd=format_usd(balance_usd),
        ))

    print("Total: %s$" % format_usd(total_usd))


def main(summary=False):
    if summary:
        print_summary()
    else:
        print_detail()


def cli():
    import argparse
    parser = argparse.ArgumentParser(description='Show cryptocoins portfilio.')
    parser.add_argument('-s', '--summary', dest='summary', action='store_true')
    args = parser.parse_args()
    main(**vars(args))
