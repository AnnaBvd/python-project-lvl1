from random import randint


TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_round():
    """Returns random question and expected answer for even game"""
    num = randint(0, 225)
    if num % 2 == 0:
        expected_answer = 'yes'
    else:
        expected_answer = 'no'
    return str(num), expected_answer
