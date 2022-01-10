from random import randint, choice


TASK = 'What is the result of the expression?'


def generate_round():
    """Returns random question and expected answer for calc game"""
    num1 = randint(0, 30)
    num2 = randint(0, 30)
    operation = choice('+-*')
    question = f'{num1} {operation} {num2}'
    expected_answer = calc(num1, num2, operation)
    return question, str(expected_answer)


def calc(num1, num2, operation):
    """Returns result of '+', '-' or '*' operations for two numbers"""
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    else:
        raise ValueError(f'Wrong or unsupported operation: {operation}')
    return result
