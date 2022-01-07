from random import randint


TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_info():
    """Returns random question and expected answer for even game"""
    think_num = randint(0, 225)
    if think_num % 2 == 0:
        expected_answer = 'yes'
    else:
        expected_answer = 'no'
    # Returns question and expected_answer needed as strings
    return str(think_num), expected_answer
