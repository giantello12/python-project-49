import prompt
import random


def generate_number():
    return random.randint(1, 100)


def greeting():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}")
    return name


def ask_answer():
    return prompt.string("Your answer: ")


def print_if_wrong_answer(answer, name, correct_answer):
    print(f"'{answer}' is wrong answer ;(.", end=' ')
    print(f"Correct answer was '{correct_answer}'")
    print(f"Let's try again, {name}!")


def print_question(arg: str):
    print(f'Question: {arg}')


def print_congratulations(name):
    print(f"Congratulations, {name}!")
