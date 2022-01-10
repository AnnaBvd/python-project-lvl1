import prompt


ROUNDS = 3


def play(game):
    """Prints all game steps, depending on game type"""
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.TASK)
    for i in range(ROUNDS):
        question, expected_answer = game.generate_round()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer != expected_answer:
            print("'{}' is wrong answer ;(. Correct answer was '{}'.".
                  format(answer, expected_answer))
            print(f"Let's try again, {name}!")
            break
        print('Correct!')
        if i == ROUNDS - 1:
            print(f"Congratulations, {name}!")
