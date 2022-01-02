import prompt
from random import randint
from brain_games.cli import welcome_user


def even_check():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 1
    # number of game rounds
    rounds_qty = 3
    while i <= rounds_qty:
        think_num = randint(0, 225)
        print('Question: {}'.format(str(think_num)))
        answer = prompt.string('Your answer: ')
        if think_num % 2 == 0:
            expected_answer = 'yes'
        else:
            expected_answer = 'no'
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
