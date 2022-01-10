from random import randint


TASK = 'Find the greatest common divisor of given numbers.'


def generate_round():
    """Returns random question and expected answer for gcd game"""
    num1 = randint(10, 120)
    num2 = randint(10, 120)
    question = f'{num1} {num2}'
    expected_answer = gcd(num1, num2)
    return question, str(expected_answer)


def gcd(num1, num2):
    """Returns greatest common divisor for two numbers"""
    for divisor in range(min(num1, num2), 0, -1):
        if num1 % divisor == 0 and num2 % divisor == 0:
            return divisor
