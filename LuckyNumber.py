import random


def lucky_number():
    name = input("What is your name? ")
    number = random.randint(1, 10)

    if number == 3 or number == 9:
        print(f"Hello {name}, your lucky number is {number} and you have won a prize.")
    elif number == 7:
        print(f"Hello {name}, your lucky number is {number} and you have hit the jackpot.")
    else:
        print(f"Hello {name}, your lucky number is {number}.")


lucky_number()
