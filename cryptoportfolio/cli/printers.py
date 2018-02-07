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


class BasePrinter:
    def __init__(self, defaults=None):
        self._cells = []
        self.defaults = defaults or {}

    def append_cell(self, name: str, crypto_balance: Decimal, crypto_decimal_places: int, usd_balance: Decimal) -> None:
        self._cells.append((
            name,
            format_curr_balance(crypto_balance, crypto_decimal_places),
            format_usd(usd_balance)
        ))

    def get_cells(self) -> Iterator[Tuple[str, Decimal, Decimal]]:
        return self._cells

    def fill_cells(self, group: List[Dict]) -> None:
        for wallet_dict in group:
            wallet = get_wallet_from_dict(wallet_dict, self.defaults)
            for symbol, balance in wallet.get_coin_tokens_balance(include_coin_balance=True):
                balance_usd = get_price_usd(symbol) * balance
                cell_name = symbol if symbol == wallet.name else "%s (%s)" % (symbol, wallet.name)
                self.append_cell(
                    cell_name,
                    balance,
                    wallet.decimal_places,
                    balance_usd
                )


def result_iterator(
        groups: Iterable[Tuple[str, List]],
        defaults: Dict
) -> Iterator[Tuple[str, Iterator[Tuple[str, Decimal, Decimal]]]]:
    for group_name, wallets in groups:
        printer = BasePrinter(defaults)
        printer.fill_cells(wallets)
        yield group_name, printer.get_cells()


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
        print("\nAll total: $%s" % format_usd(all_total))
