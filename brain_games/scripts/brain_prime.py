#!/usr/bin/env python
"""Is-prime game"""

from brain_games.games import prime
from brain_games.game_logic import play_game


def main():
    """Runs "brain-prime" (is-prime) game"""
    play_game(prime)


if __name__ == "__main__":
    main()
