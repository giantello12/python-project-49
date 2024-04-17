#!/usr/bin/env python3

import brain_games.engine


def is_correct(answer, cor_answer):
    if answer == cor_answer:
        return True
    return False


def main():
    name = brain_games.engine.greeting()
    print("What number is missing in the progression?")
    attempts = 3
    for _ in range(attempts):
        cor_answer = brain_games.engine.make_progression()
        answer = brain_games.engine.ask_answer()
        if is_correct(answer, cor_answer):
            print('Correct!')
        else:
            brain_games.engine.print_if_wrong_answer(answer, name, cor_answer)
            break

    else:
        print(f'Congratulations, {name}!')


if __name__ == "__main__":
    main()
