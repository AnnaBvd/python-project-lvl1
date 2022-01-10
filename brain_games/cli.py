import prompt


def welcome_user():
    """Greets user and returns their input name"""
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name
