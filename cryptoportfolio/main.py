#!/usr/bin/python
import importlib.machinery
from decimal import Decimal

from cryptoportfolio.utils.io import table

from cryptoportfolio.lib.coinmarketcap import get_price_usd
from cryptoportfolio.utils.io import format_usd, format_curr_balance


def print_detail(settings):
    total_usd = Decimal('0.00000')
    cells = []

    for wallet in settings.WALLETS:
        cells.append((wallet.get_name(), '', ''))
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
            cells.append((symbol, format_curr_balance(balance, decimal_places), "$%s" % format_usd(balance_usd)))
    print(table(cellgrid=cells))
    print("Total: %s$" % format_usd(total_usd))


def print_summary(settings):
    total_usd = Decimal('0.0')

    curr_dict = {}
    for wallet in settings.WALLETS:
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
    cells = []
    for symbol, data in reversed(sorted(curr_dict.items(), key=lambda x: x[1]['balance_usd'])):
        balance = data['balance']
        balance_usd = data['balance_usd']
        decimal_places = data['decimal_places']
        total_usd += balance_usd
        cells.append((symbol, format_curr_balance(balance, decimal_places), "$%s" % format_usd(balance_usd)))
    print(table(cellgrid=cells))
    print("Total: %s$" % format_usd(total_usd))


def main(settings_path, summary=False):
    settings = importlib.machinery.SourceFileLoader('settings', settings_path).load_module()

    if summary:
        print_summary(settings)
    else:
        print_detail(settings)


def cli():
    import argparse
    parser = argparse.ArgumentParser(description='Show cryptocoins portfilio.')
    parser.add_argument('settings_path', type=str)
    parser.add_argument('-s', '--summary', dest='summary', action='store_true')
    args = parser.parse_args()
    main(**vars(args))
