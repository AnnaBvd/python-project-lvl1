#!/usr/bin/env python
"""Is-prime game"""

from brain_games.games import prime
from brain_games.engine import play


def main():
    """Runs "brain-prime" (is-prime) game"""
    play(prime)


if __name__ == "__main__":
    main()
