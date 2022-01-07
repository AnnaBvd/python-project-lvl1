from random import randint, choice


TASK = 'What is the result of the expression?'


def get_info():
    """Returns random question and expected answer for calc game"""
    first_num = randint(0, 30)
    second_num = randint(0, 30)
    # only +, -, * operations used
    oper = choice('+-*')
    if oper == '+':
        expected_answer = str(first_num + second_num)
    elif oper == '-':
        expected_answer = str(first_num - second_num)
    else:
        expected_answer = str(first_num * second_num)
    question = '{} {} {}'.format(str(first_num), oper, str(second_num))
    return question, expected_answer
