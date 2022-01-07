from random import randint


TASK = 'What number is missing in the progression?'


def get_info():
    """Returns random question and expected answer for progression game"""
    progr_length = randint(5, 11)
    progr_start = randint(2, 33)
    step = randint(2, 7)
    progr_list = [progr_start]
    # start from 1 because we already have progr_start on index 0
    i = 1
    while i < progr_length:
        progr_list.append(progr_list[i - 1] + step)
        i += 1
    # pick random index
    hidden_position = randint(0, progr_length - 1)
    expected_answer = str(progr_list[hidden_position])
    progr_list[hidden_position] = '..'
    # convert modified list to a string
    question = ' '.join(str(i) for i in progr_list)
    return question, expected_answer
