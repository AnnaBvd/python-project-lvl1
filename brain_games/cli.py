import prompt


def welcome_user():
    """Greets user and returns their input name"""
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    return name
