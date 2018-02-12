from copy import deepcopy
from decimal import Decimal
from typing import List, Dict, Tuple, Iterator, Iterable

from cryptoportfolio.utils.io import table
from cryptoportfolio.interfaces import INTERFACES_MAPPING
from cryptoportfolio.interfaces.base import Address
from cryptoportfolio.lib.coinmarketcap import get_price_usd
from cryptoportfolio.utils.io import format_curr_balance, format_usd


def get_wallet_from_dict(wallet_data: Dict, defaults: Dict) -> Address:
    data = deepcopy(defaults)
    data.update(wallet_data)
    assert 'interface' in data

    interface = data.pop('interface')
    if interface not in INTERFACES_MAPPING:
        raise ValueError("Unknown interface: %s" % interface)

    return INTERFACES_MAPPING[interface](**data)


def address_query(wallets: List[Dict], defaults) -> Iterator[Tuple[str, Decimal, Decimal]]:
    for wallet_dict in wallets:
        wallet = get_wallet_from_dict(wallet_dict, defaults)
        for symbol, balance in wallet.get_coins_and_tokens_balance():
            balance_usd = get_price_usd(symbol) * balance
            if wallet.name is not None:
                cell_name = "%s (%s)" % (symbol, wallet.name)
            else:
                cell_name = symbol
            yield (
                cell_name,
                format_curr_balance(balance, wallet.decimal_places),
                format_usd(balance_usd)
            )


def result_iterator(
        groups: Iterable[Tuple[str, List]],
        defaults: Dict
) -> Iterator[Tuple[str, Iterator[Tuple[str, Decimal, Decimal]]]]:
    for group_name, wallets in groups:
        yield group_name, address_query(wallets, defaults)


def summarize_cells(
        groups: Iterator[Tuple[str, Iterator[Tuple[str, Decimal, Decimal]]]]
) -> Iterator[Tuple[str, Iterable[Tuple[str, Decimal, Decimal]]]]:
    for group_name, cells in groups:
        group_names: Dict = {}
        for name, coins, usd_coins in cells:
            if name not in group_names:
                group_names[name] = {
                    'coins': Decimal('0.00'),
                    'usd_coins': Decimal('0.00'),
                }
            group_names[name]['coins'] += coins
            group_names[name]['usd_coins'] += usd_coins
        yield group_name, [(name, x['coins'], x['usd_coins']) for name, x in group_names.items()]


def hide_zeros_cells(
        groups: Iterator[Tuple[str, Iterator[Tuple[str, Decimal, Decimal]]]]
) -> Iterator[Tuple[str, Iterator[Tuple[str, Decimal, Decimal]]]]:
    for group_name, cells in groups:
        yield group_name, filter(lambda x: x[1] != Decimal('0.00'), cells)


def hide_usd_zeros_cells(
        groups: Iterator[Tuple[str, Iterator[Tuple[str, Decimal, Decimal]]]]
) -> Iterator[Tuple[str, Iterator[Tuple[str, Decimal, Decimal]]]]:
    for group_name, cells in groups:
        yield group_name, filter(lambda x: x[2] != Decimal('0.00'), cells)


def sort_cells(
        groups: Iterator[Tuple[str, Iterator[Tuple[str, Decimal, Decimal]]]]
) -> Iterator[Tuple[str, Iterator[Tuple[str, Decimal, Decimal]]]]:
    for group_name, cells in groups:
        yield group_name, reversed(sorted(cells, key=lambda x: x[2]))


def print_results(
        groups: Iterator[Tuple[str, Iterator[Tuple[str, Decimal, Decimal]]]],
        print_all_total,
        print_group_total
) -> None:
    all_total = Decimal('0.00')

    for group_name, cells in groups:
        list_cells = list(cells)
        group_total = sum(x[2] for x in list_cells)
        all_total += group_total
        if len(list_cells):
            print(table(title=group_name, cellgrid=list_cells))
            if print_group_total:
                print("Total: $%s" % format_usd(group_total))

    if print_all_total:
        print("All total: $%s" % format_usd(all_total))
