from random import randint


TASK = 'What number is missing in the progression?'


def generate_round():
    """Returns random question and expected answer for progression game"""
    first = randint(2, 33)
    diff = randint(2, 7)
    length = randint(5, 11)
    progr_list = generate_progression(first, diff, length)
    hidden_position = randint(0, length - 1)
    expected_answer = progr_list[hidden_position]
    progr_list[hidden_position] = '..'
    question = ' '.join(str(i) for i in progr_list)
    return question, str(expected_answer)


def generate_progression(first, diff, length):
    """Generates arithmetic progression list"""
    progr_list = [first]
    for i in range(1, length):
        progr_list.append(progr_list[i - 1] + diff)
    return progr_list
