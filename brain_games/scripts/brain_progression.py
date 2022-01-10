#!/usr/bin/env python
"""Arithmetic progression with unknown number game"""

from brain_games.games import progression
from brain_games.engine import play


def main():
    """Runs "brain-progression" (arithmetic with unknown member) game"""
    play(progression)


if __name__ == "__main__":
    main()
