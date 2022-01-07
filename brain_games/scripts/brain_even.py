#!/usr/bin/env python
"""Is-even game"""

from brain_games.games import even
from brain_games.game_logic import play_game


def main():
    """Runs "brain-even" (is-even) game"""
    play_game(even)


if __name__ == "__main__":
    main()
