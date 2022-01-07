from random import randint


TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_info():
    think_num = randint(2, 60)
    question = str(think_num)
    # initialize expected_answer for using it after the loop
    expected_answer = ''
    divider = 2
    # dividers from 2 till sqrt(think_num) are enough
    while divider <= think_num ** (0.5):
        if think_num % divider == 0:
            expected_answer = 'no'
            break
        divider += 1
    if expected_answer == '':
        expected_answer = 'yes'
    return question, expected_answer
