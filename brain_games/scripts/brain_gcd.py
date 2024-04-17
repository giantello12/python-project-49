#!/usr/bin/env python3

import brain_games.engine


def is_correct(answer, result):
    if answer == result:
        return True
    return False


def main():
    name = brain_games.engine.greeting()
    print('Find the greatest common divisor of given numbers.')
    attempts = 3
    for _ in range(attempts):
        num1 = brain_games.engine.generate_number()
        num2 = brain_games.engine.generate_number()
        result = brain_games.engine.find_gcd(num1, num2)
        arg = f'{str(num1)} {str(num2)}'
        brain_games.engine.print_question(arg)
        answer = brain_games.engine.ask_answer()
        if is_correct(int(answer), result):
            print('Correct!')
        else:
            brain_games.engine.print_if_wrong_answer(answer, name, result)
            break
    else:
        print(f'Congratulations, {name}!')


if __name__ == "__main__":
    main()
