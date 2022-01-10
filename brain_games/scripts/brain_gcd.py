#!/usr/bin/env python
"""Greatest common divisor game"""

from brain_games.games import gcd
from brain_games.engine import play


def main():
    """Runs "brain-gcd" (greatest common divisor) game"""
    play(gcd)


if __name__ == "__main__":
    main()
