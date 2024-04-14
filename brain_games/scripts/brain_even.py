#!/usr/bin/env python3

import random
import prompt


def generate_number():
    return random.randint(1, 100)


def is_correct(answer: str, num: int) -> bool:
    if num % 2 == 0 and answer == "yes" or num % 2 != 0 and answer == "no":
        return True
    return False


def ask_name():
    return prompt.string("May I have your name? ")


def main():
    print("Welcome to the Brain Games!")
    name = ask_name()
    print(f"Hello, {name}")
    print('Answer "yes" if number is even, otherwise answer "no"')

    for _ in range(3):
        num = generate_number()
        print(f'Question: {num}')
        answer = prompt.string("Your answer: ")
        if is_correct(answer, num):
            print('Correct!')
        else:
            correct_answer = "'yes'" if answer == "no" else "'no'"
            print(f"'{answer}' is wrong answer ;(.", end=' ')
            print(f"Correct answer was '{correct_answer}'")
            print(f"Let's try again, {name}!")
            break
    else:
        print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
