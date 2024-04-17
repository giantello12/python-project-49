#!/usr/bin/env python3

import brain_games.engine


def is_correct(answer: str, num: int) -> bool:
    if num % 2 == 0 and answer == "yes" or num % 2 != 0 and answer == "no":
        return True
    return False


def main():
    name = brain_games.engine.greeting()
    attempts = 3
    print('Answer "yes" if the number is even, otherwise answer "no".')

    for _ in range(attempts):
        num = brain_games.engine.generate_number()
        brain_games.engine.print_question(str(num))
        answer = brain_games.engine.ask_answer()

        if is_correct(answer, num):
            print('Correct!')
        else:
            cor_answer = "yes" if answer == "no" else "no"
            brain_games.engine.print_if_wrong_answer(answer, name, cor_answer)
            break

    else:
        brain_games.engine.print_congratulations(name)


if __name__ == "__main__":
    main()
