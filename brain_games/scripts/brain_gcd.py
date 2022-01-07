#!/usr/bin/env python
"""Greatest common divisor game"""

from brain_games.games import gcd
from brain_games.game_logic import play_game


def main():
    """Runs "brain-gcd" (greatest common divisor) game"""
    play_game(gcd)


if __name__ == "__main__":
    main()
