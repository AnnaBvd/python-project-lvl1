#!/usr/bin/env python
"""Arithmetic progression with unknown number game"""

from brain_games.games import progression
from brain_games.game_logic import play_game


def main():
    """Runs "brain-progression" (arithmetic with unknown member) game"""
    play_game(progression)


if __name__ == "__main__":
    main()
