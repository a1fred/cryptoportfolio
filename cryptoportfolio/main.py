#!/usr/bin/python
import sys
from yaml import BaseLoader

from cryptoportfolio.cli.printers import (
    result_iterator,
    summarize_cells,
    hide_zeros_cells,
    hide_usd_zeros_cells,
    sort_cells,
    print_results,
)

from cryptoportfolio.lib.convert import CONVERTORS_MAPPING


def main(settings_path, summarize, hide_zeros, hide_usd_zeros, sort, print_all_total, print_group_total):
    import yaml
    settings = yaml.load(settings_path, BaseLoader)
    settings_path.close()

    try:
        defaults = settings.get('defaults', {})
        groups = settings.get('groups', {})
        tickers = settings.get('tickers', {})
        converting = settings.get('converting', 'coinmarketcap')
    except AttributeError:
        # AttributeError: 'str' object has no attribute 'get' raises if wrong file type
        print("Wrong configuration file type")
        return

    if converting not in CONVERTORS_MAPPING:
        print("Unknown convetror %s, possible values are: %s" % (
            converting,
            "|".join(CONVERTORS_MAPPING.keys())
        ))
        sys.exit(1)
    else:
        get_price_usd = CONVERTORS_MAPPING[converting]

    if not groups and not tickers:
        print("No groups and no tickers is defined. Exiting.")

    results = result_iterator(groups.items(), defaults, get_price_usd)
    if summarize:
        results = summarize_cells(results)
    if hide_zeros:
        results = hide_zeros_cells(results)
    if hide_usd_zeros:
        results = hide_usd_zeros_cells(results)
    if sort:
        results = sort_cells(results)

    print_results(results, print_all_total=print_all_total, print_group_total=print_group_total)

    if tickers:
        print("\nTickers:")
        for symbol in tickers:
            print(" * %-4s $%s" % (symbol, get_price_usd(symbol)))


def cli():
    import argparse
    parser = argparse.ArgumentParser(description='Show cryptocoins portfilio.')
    parser.add_argument('settings_path', type=argparse.FileType('r'))
    parser.add_argument('-s', '--summarize', action='store_true', help="Summarize same currencies in one row")
    parser.add_argument('-z', '--hide-zeros', action='store_true', help="Hide zero crypto balances")
    parser.add_argument('--sort', action='store_true', help="Sort by USD balance")
    parser.add_argument('--hide-usd-zeros', action='store_true', help="Hide zero USD balances")
    parser.add_argument('-T', '--print-all-total', action='store_true', help="Print all total USD")
    parser.add_argument('-t', '--print-group-total', action='store_true', help="Print group total USD")
    args = parser.parse_args()
    main(**vars(args))
