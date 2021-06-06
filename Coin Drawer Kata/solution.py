from __future__ import annotations

import random
from collections import defaultdict

class EmptyDrawer(Exception):
    pass

COINS: dict[int, int] = {
    25: 10,
    10: 10,
    5: 10,
    1: 10,
}

COIN_NAMES: dict[int, str] = {
    25: 'quarters',
    10: 'dimes',
    5: 'nickels',
    1: 'pennies',
}


def total():
    """Produce a random purchase amount."""
    return round(random.random() * 1000, 2)


def calculate_change(total: float) -> float:
    """Determine how much change is needed."""
    return round(1 - (total - int(total)), 2)


def determine_coins(change: float) -> dict[int, int]:
    """Determine how many coins of each type to return."""
    remaining = int(change * 100)
    _coins = defaultdict(int)

    for value, count in COINS.items():
        while remaining >= value and COINS[value]:
            _coins[value] += 1
            COINS[value] -= 1
            remaining -= value

    if remaining:
        raise EmptyDrawer("You don't have enough coins to make the change!")
    return _coins


def help_customer():
    """Handle a customer transaction."""
    _total = total()
    _change = calculate_change(_total)
    _coins = determine_coins(_change)

    print(f"A transaction of {_total} requires {_change} in coins:")
    for value, count in _coins.items():
        print(f"{COIN_NAMES[value]}: {count}")


if __name__ == "__main__":
    for _ in range(10):
        help_customer()
