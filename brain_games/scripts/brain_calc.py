#!/usr/bin/env python
"""Calculator game"""

from brain_games.games import calc
from brain_games.engine import play


def main():
    """Runs "brain-calc" (calculator) game"""
    play(calc)


if __name__ == "__main__":
    main()
