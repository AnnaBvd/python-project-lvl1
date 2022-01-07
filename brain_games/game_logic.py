import prompt
from brain_games.cli import welcome_user


def play_game(game):
    """Prints all game steps, depending on game type"""
    name = welcome_user()
    print(game.TASK)
    i = 1
    # number of game rounds
    rounds_qty = 3
    while i <= rounds_qty:
        question, expected_answer = game.get_info()
        print('Question: {}'.format(question))
        answer = prompt.string('Your answer: ')
        if answer != expected_answer:
            # wrong answer
            print("'{}' is wrong answer ;(. Correct answer was '{}'.".
                  format(answer, expected_answer))
            print("Let's try again, {}!".format(name))
            break
        print('Correct!')
        # game finish
        if i == rounds_qty:
            print("Congratulations, {}!".format(name))
        i += 1
