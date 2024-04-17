#!/usr/bin/env python3

import brain_games.engine


def is_correct(answer, cor_answer):
    if answer == cor_answer:
        return True
    return False


def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def main():
    name = brain_games.engine.greeting()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    attempts = 3
    for _ in range(attempts):
        num = brain_games.engine.generate_number()
        brain_games.engine.print_question(str(num))
        answer = brain_games.engine.ask_answer()
        cor_answer = 'yes' if is_prime(num) else 'no'
        if is_correct(answer, cor_answer):
            print('Correct!')
        else:
            brain_games.engine.print_if_wrong_answer(answer, name, cor_answer)
            break
    else:
        print(f'Congratulations, {name}!')


if __name__ == "__main__":
    main()
