from random import randint


TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_round():
    """Returns random question and expected answer for prime number game"""
    num = randint(2, 60)
    question = str(num)
    expected_answer = 'yes' if is_prime(num) else 'no'
    return question, expected_answer


def is_prime(num):
    for divisor in range(2, int(num ** 0.5) + 1):
        if num % divisor == 0:
            return False
    return True
