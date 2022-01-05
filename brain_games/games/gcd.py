from random import randint


TASK = 'Find the greatest common divisor of given numbers.'


def get_info():
    first_num = randint(10, 120)
    second_num = randint(10, 120)
    if first_num > second_num:
        divider = second_num
    else:
        divider = first_num
    while divider > 0:
        if first_num % divider == 0 and second_num % divider == 0:
            expected_answer = str(divider)
            break
        divider -= 1
    question = '{} {}'.format(str(first_num), str(second_num))
    return question, expected_answer